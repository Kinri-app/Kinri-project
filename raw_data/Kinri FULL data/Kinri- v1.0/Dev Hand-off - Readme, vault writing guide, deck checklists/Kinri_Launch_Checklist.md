# Kinri Product Launch Checklist

This checklist ensures all core systems are ready for Kinri’s MVP release.

---

## Product Core

- Vault Cards — Fully uploaded and validated
- Scoring Logic — Built and tested with output examples
- Echo Tone Map — Core delivery tones mapped and aligned with response logic
- API + Retrieval — /getVaultCard endpoint operational with tag/condition filtering
- My Vault — Resonance scoring and feedback logic finalized
- Suggestions & Journaling — Triggers connected to user inputs

---

## Developer Setup

- Vault Schema — Imported into database successfully
- Retrieval Endpoint — Returns correct VaultCard JSON format
- Echo Delivery Logic — Implemented and functional on frontend
- Journaling Tag Pipeline — Working end-to-end from user input to DB
- User Feedback System — Captures card responses and emotion tags
- Error Handling — Fallback flows functional when no matches returned

---

## UX / UI

- Vault Card Display — Shows intro, body, prompt if present
- Reaction Options — ❤️ / 🔁 / 😐 / 📌 / 📝 buttons functional
- Vault Explorer (Optional) — Card browser and tag search working
- Daily Echo Prompt — Configured and displayed (if enabled)
- Saved Vault View — Allows users to filter and review past cards

---

## Trust & Safety

- Vault Content Review — Trigger-sensitive cards checked and tagged
- Journaling Privacy Policy — Visible and up-to-date
- Echo Disclaimer — Included on card delivery (“This is not therapy”)
- Data Storage — Secured and compliant (e.g. Supabase or Firebase)

---

## Launch Bonuses (Optional)

- Email System — Ready for onboarding and user communication
- Bug Report Link — Live and functional
- Post-Card Feedback — “What helped you today?” prompt working
- Onboarding Flow — “What do you want Kinri to help you with?” captures goal