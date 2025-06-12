# Kinri Flashcard Archive — Developer Reference

This folder contains Kinri’s flashcards. These are short, standalone insight cards designed for user self-learning and quiet reflection.

They are **not** used by the Echo system in conversational flows.

---

## Format

Two types of JSON structures exist:

### 1. Q&A format
```json
{
  "question": "...",
  "answer": "...",
  "tags": [...]
}
```

### 2. Headline + Prompt format
```json
{
  "headline": "...",
  "body": "...",
  "prompt": "...",
  "tags": [...]
}
```

---

## MVP Usage

- Users browse these flashcards independently (outside of Echo)
- Flashcards should be filterable by tag (e.g. ADHD, Shame)
- All files are static and non-interactive

---

## Current Limitations

- Tags are inconsistent across files
- No metadata (e.g. card id, timestamps)
- No linking between flashcards and Vaults
- Some cards may overlap or repeat

---

## Optional Improvements (Post-MVP)

These aren’t required now, but would improve long-term function:

- Add metadata fields (id, date_created, etc.)
- Standardize tag vocabulary
- Let users favorite or flag flashcards
- Allow Echo to recommend flashcards during sessions

---

## Summary

Flashcards are Kinri’s quiet learning mode.
They’re for exploring truth slowly — not for deep emotional dialogue.

They should be accessible, searchable, and safe to explore.