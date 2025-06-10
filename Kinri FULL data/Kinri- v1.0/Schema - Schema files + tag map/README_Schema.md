# Kinri Schema Files

This folder contains structural and logic reference files for the Kinri MVP.

## Files Included:

- `VaultCardSchema.odt`  
  → Main schema document describing the expected structure and required fields for all Echo-compatible Vault cards.

- `SymptomTag_Translator_Map.csv`  
  → Mapping matrix that translates symptom keywords or flags into condition tags. Used for tag inference and vault retrieval logic.

- `Kinri_Vault_Retrieval_Dev_Schema.odt`  
  → Retrieval design logic for how Echo fetches contextually appropriate Vault cards based on session state and user profile.

- `LastState_Tracker_Schema.odt`  
  → Tracks Echo's memory of the user's last interaction, emotion, or condition context for continuity across sessions.

Each schema supports different components of the Kinri Engine — together they ensure emotional intelligence, consistency, and traceability.