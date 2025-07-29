# Kinri: Trauma-Informed Diagnostic Engine

**Status**: In Development — Sprint 3  
**Branch**: `develop`  

---

## 📌 Project Overview

Kinri is a trauma-informed diagnostic tool designed to guide users through a multi-stage self-reflection process. The goal is to generate personalized insights using Vault cards (pre-written emotional support statements) based on user responses across three diagnostic stages.

The system leverages Retrieval-Augmented Generation (RAG) to map responses to relevant insight cards. Long-term, it will support downstream training for large language models (LLMs) and help drive emotionally aware health tech solutions.

---

## 🎯 MVP Goals

-   Deliver a 3-stage reflection flow per user
-   Retrieve relevant insight cards based on tag-matching
-   Generate JSON session exports for future LLM training
-   Validate data quality and flow logic through QA

---

## 🧱 Project Structure
```

kinri-app/
├── backend/ # Flask API, Supabase client, business logic
│ ├── app/
│ ├── run.py
│ ├── requirements.txt
│ └── .venv/ # Python virtual environment
├── frontend/ # Vite + React TypeScript app
│ ├── src/
│ ├── index.html
│ └── package.json
├── raw_data/ # Original Vault card JSONs & user session exports
├── Makefile # Automates setup and run tasks
└── README.md # Project overview and instructions

````

---

## 🖥️ How to Run the Project on Windows

This project uses a Makefile to automate setup and execution. Follow the steps below to run it on a Windows machine:

### 1. Requirements

Ensure you have the following installed:

- [Python 3.12+](https://www.python.org/downloads/)
- [Node.js 18+ and npm](https://nodejs.org/)
- A terminal that supports `make` (such as Git Bash or WSL).
  If not, you can install [GnuWin Make](http://gnuwin32.sourceforge.net/packages/make.htm) or use WSL.

---

### 2. Environment Files Required

Both the frontend and backend require `.env` files to run.

> These files are **not included** in the repository. Please reach out to a project maintainer (e.g., Bryan Lazo or Mikey Torres) to request the `.env` files for development.

Once received:
- Place the `.env` file in the `backend/` directory for Flask.
- Place the `.env` file in the `frontend/` directory for Vite.

---

### 3. Available Makefile Commands

Run the following command to see available options:

```bash
make help
````

This will list:

-   `make setup` – Set up both frontend and backend
-   `make run` – Run both frontend and backend concurrently
-   `make run-backend` – Run only the Flask backend
-   `make run-frontend` – Run only the React frontend
-   `make setup-backend` – Set up Python virtual environment and install backend dependencies
-   `make setup-frontend` – Install frontend dependencies using npm

---

### 4. First-Time Setup

Run this command from the project root:

```bash
make setup
```

This will:

-   Create a virtual environment in `backend/.venv`
-   Install Python packages listed in `backend/requirements.txt`
-   Install frontend dependencies via `npm install`

---

### 5. Run the App

After setup and placing the `.env` files:

```bash
make run
```

This will:

-   Start the Flask backend at `http://127.0.0.1:5000/`
-   Start the React frontend at `http://localhost:5173/`

Logs from both will appear in your terminal, labeled `[BACKEND]` and `[FRONTEND]`.

---

## 🔐 Project Roles

| Role              | Name                           |
| ----------------- | ------------------------------ |
| Product Owner     | ASA                            |
| Frontend Engineer | Ryan Boll & Bryan Lazo         |
| Backend Engineers | Ryan Boll & Bryan Lazo         |
| Cybersecurity     | Gabriel Valencia & Howard Bush |
| Data Analyst      | Mikey Torres                   |