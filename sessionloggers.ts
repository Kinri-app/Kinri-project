// sessionLogger.ts

import EncryptedStorage from 'react-native-encrypted-storage';
import { Platform } from 'react-native';
import { createClient } from '@supabase/supabase-js';

// Initialize Supabase client
const supabase = createClient(
  process.env.EXPO_PUBLIC_SUPABASE_URL!,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY!
);

// TypeScript interface
export interface SessionLog {
  sessionId: string;
  timestamp: string;
  event:
    | 'AUTH_SUCCESS'
    | 'SESSION_INIT'
    | 'QUESTION_ANSWERED'
    | 'VAULT_CARD_DELIVERED'
    | 'LLM_PROMPT_GENERATED'
    | 'JSON_EXPORT_TRIGGERED';
  questionId?: string;
  responseValue?: number;
  scoreDelta?: number;
  metadataTags?: string[];
  deviceId: string;
  promptTemplateHash?: string;
  appVersion: string;
  platform: 'iOS' | 'Android' | 'Web';
  authContext: {
    authProvider: string;
    userUid: string;
  };
  ip_hash?: string;
}

// Store securely (AES-256 via OS keystore)
export async function storeSession(session: object) {
  try {
    await EncryptedStorage.setItem('kinri_session', JSON.stringify(session));
  } catch (error) {
    console.error('🔐 Secure store error:', error);
  }
}

// Retrieve securely
export async function getSession(): Promise<any | null> {
  try {
    const data = await EncryptedStorage.getItem('kinri_session');
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('🔓 Secure retrieve error:', error);
    return null;
  }
}

// Clear session
export async function clearSession() {
  try {
    await EncryptedStorage.removeItem('kinri_session');
  } catch (error) {
    console.error('🗑️ Secure clear error:', error);
  }
}

// Unified event logger
export async function logEvent(
  eventType: SessionLog['event'],
  partial: Partial<SessionLog>
): Promise<void> {
  try {
    const sessionId = (await EncryptedStorage.getItem('kinri_session_id')) || 'unknown';
    const userUid = (await EncryptedStorage.getItem('supabase_uid')) || 'anonymous';
    const deviceId = (await EncryptedStorage.getItem('device_id')) || 'device-unknown';

    const payload: SessionLog = {
      sessionId,
      timestamp: new Date().toISOString(),
      event: eventType,
      deviceId,
      appVersion: '1.1.0',
      platform: Platform.OS === 'ios' ? 'iOS' : 'Android',
      authContext: {
        authProvider: 'supabase',
        userUid
      },
      ...partial
    };

    const { error } = await supabase.from('session_logs').insert([payload]);
    if (error) console.warn('📉 Failed to log event:', error.message);
  } catch (err) {
    console.error('🔥 Unexpected logging error:', err);
  }
}
