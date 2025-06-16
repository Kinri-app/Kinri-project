# 🌿 Kinri Backend

This repository contains the **backend** for the **Kinri project**, built with **Flask**, **SQLAlchemy**, and managed via **Docker** and **Make** for ease of development and deployment.

---

## 📦 Prerequisites

Before you start, make sure you have the following installed:

* 🐳 [Docker](https://docs.docker.com/get-docker/)
* 🛠️ [Make](https://www.gnu.org/software/make/) (optional but recommended)
* 📄 (Optional) `.env` file for custom database configuration:

  ```
  DATABASE_URL=postgresql://postgres:postdev@db:5432/kinri_db
  ```

---

## 🪟 Quick Guide: Install Make on Windows

If you're using **Windows** and don’t have `make`, install it with one of these options:

### Option 1 – Chocolatey (Recommended)

1. Install [Chocolatey](https://chocolatey.org/install) (run in PowerShell as Administrator):

   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; `
   [System.Net.ServicePointManager]::SecurityProtocol = `
     [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
   iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

2. Then install `make`:

   ```powershell
   choco install make
   ```

3. Restart your terminal.

### Option 2 – Git Bash

Use [Git Bash](https://gitforwindows.org/) which includes a version of `make`.

---

## 🧠 Project Overview

```
backend/
│
├── app/                  → Main Flask application code
│   ├── __init__.py       → App factory, DB setup
│   └── routes.py         → API routes (root health check)
│
├── config.py             → App configuration using .env variables
├── run.py                → Entry point to run the app
│
├── requirements.txt      → Python dependencies
├── Dockerfile            → Builds the backend service image
├── docker-compose.yml    → Orchestrates API and DB services
└── Makefile              → Useful CLI shortcuts
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone git@github.com:Mtorres2562/Kinri-project.git
cd Kinri-project/backend
```

### 2️⃣ Build the Containers

```bash
make build
```

### 3️⃣ Start the Project

```bash
make start
```

This will spin up two services:

| Service | Description                    | Port   |
| ------- | ------------------------------ | ------ |
| `api`   | Flask backend (auto-reloading) | `5000` |
| `db`    | PostgreSQL database            | `5432` |

### 4️⃣ Visit the API

Go to: 👉 [http://localhost:5000](http://localhost:5000)

---

## 🔁 Live API Reload

✅ When you change your backend code, it will **automatically reload** on the next request.

⚠️ If the changes **don’t appear**, run:

```bash
make restart
```

---

## 🧰 Handy Make Commands

| Command        | Description                                  |
| -------------- | -------------------------------------------- |
| `make build`   | Build Docker images                          |
| `make start`   | Start containers in detached mode            |
| `make stop`    | Stop running containers                      |
| `make restart` | Restart all services                         |
| `make clean`   | Stop containers, remove volumes and networks |
| `make ssh-api` | Open a shell in the Flask API container      |
| `make ssh-db`  | Open a shell in the PostgreSQL DB container  |

---

## 🧪 Run Locally Without Docker

> For advanced users who prefer a non-container workflow.

1. Ensure Python 3.12 is installed.
2. Create and activate a virtual environment:

```bash
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set the `DATABASE_URL` environment variable:

```bash
# Linux/Mac
export DATABASE_URL=postgresql://postgres:postdev@localhost:5432/kinri_db
# Windows PowerShell
$env:DATABASE_URL="postgresql://postgres:postdev@localhost:5432/kinri_db"
```

5. Run the app:

```bash
python run.py
# or
flask run --host=0.0.0.0 --port=5000
```