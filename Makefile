# Makefile for Kinri App

# Variables
BACKEND_DIR=backend
FRONTEND_DIR=frontend
PYTHON=python3
PIP=pip

# Help command
help:
	@echo "Available commands:"
	@echo "  make help             Show this help message"
	@echo "  make setup            Set up both frontend and backend"
	@echo "  make setup-backend    Set up backend virtual environment and install dependencies"
	@echo "  make setup-frontend   Install frontend dependencies"
	@echo "  make run-backend      Run backend server (Flask)"
	@echo "  make run-frontend     Run frontend development server (Vite/React)"

# Setup backend
setup-backend:
	@echo "Setting up Python virtual environment and installing dependencies..."
	@cd $(BACKEND_DIR) && $(PYTHON) -m venv .venv
	@cd $(BACKEND_DIR) && .venv/bin/$(PIP) install -r requirements.txt

# Run backend
run-backend:
	@echo "Starting backend..."
	@cd $(BACKEND_DIR) && source .venv/bin/activate && flask run --reload --port 5001

# Setup frontend
setup-frontend:
	@echo "Installing frontend dependencies..."
	@cd $(FRONTEND_DIR) && npm install

# Run frontend
run-frontend:
	@echo "Starting frontend..."
	@cd $(FRONTEND_DIR) && npm run dev

run:
	@echo "Running frontend and backend concurrently..."
	@cd $(FRONTEND_DIR) && npm install concurrently cross-env --save-dev
	@cd $(FRONTEND_DIR) && npx concurrently -n BACKEND,FRONTEND -c red,cyan \
		"cd ../$(BACKEND_DIR) && source .venv/bin/activate && FLASK_APP=run.py FLASK_ENV=development flask run --reload --port 5001" \
		"npm run dev"

# Full setup
setup: setup-backend setup-frontend
	@echo "Setup complete. You can now run the project with 'make run'"
