# 🧠 Kinri: Trauma-Informed Diagnostic Engine

> **Status:** 🚧 In Development — Sprint 3  
> **Branch:** `develop`  
> **Lead Analyst:** Mikey Torres  

---

## 📌 Project Overview

Kinri is a trauma-informed diagnostic tool designed to guide users through a multi-stage self-reflection process. The goal is to generate personalized insights using Vault cards (pre-written emotional support statements) based on user responses across three diagnostic stages.

The system leverages **Retrieval-Augmented Generation (RAG)** to map responses to relevant insight cards. Long-term, it will support downstream training for LLMs and help drive emotionally aware health tech solutions.

---

## 🎯 MVP Goals

- Deliver a 3-stage reflection flow per user
- Retrieve relevant insight cards based on tag-matching
- Generate JSON session exports for future LLM training
- Validate data quality and flow logic through QA

---

## 🧱 Project Structure

Kinri-project/
│
├── backend/                    # Dev-related system files (optional, or move contents to docs/)
│   └── kinri_architecture.png  # Exported Lucidchart diagram
│
├── data/                       # Transformed / cleaned data outputs
│
├── raw_data/                   # Original Vault card JSONs & user session exports
│
├── docs/                       # Project documentation and diagrams
│   ├── rag_overview.md         # (Future) Notes on RAG implementation
│   ├── kpi_matrix.md           # (Future) Draft KPI table
│   └── scoring_logic.md        # (Optional) Diagnostic logic explained
│
├── Notebooks/                  # Jupyter notebooks
│   ├── json_validation.ipynb
│   └── rag_retrieval.ipynb
│
└── README.md                   # Primary project overview (linked to docs/)

## 🔐 Roles

| Role | Name |
|------|------|
| Product Owner | ASA |
| Frontend Engineer | Curtis Pierce |
| Backend Engineer | Ryan Boll & Bryan Lazo |
| Cybersercurity | Gabriel Valencia & Howard Bush |
| Data Analyst | Mikey Torres ✅ |

## 🙋‍♀️ Interested in Contributing?

We’re a multi-disciplinary team building something with heart. If you’re passionate about trauma-informed tech, reach out or fork the repo!