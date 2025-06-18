# Variables
DOCKER_NETWORK = kinri_network
API_CONTAINER = backend-api-1
DB_CONTAINER = backend-db-1

.PHONY: start stop restart build clean ssh-api ssh-db run

start: ## Start containers in detached mode
	docker-compose up

stop: ## Stop running containers
	docker-compose stop

restart: ## Restart containers
	$(MAKE) stop
	$(MAKE) start

build: ## Build images
	docker-compose build

clean: ## Stop containers and remove volumes, network, orphans, and prune images
	docker-compose down -v --remove-orphans
	-docker network rm $(DOCKER_NETWORK)
	docker image prune -f

ssh-api: ## Open bash shell in Flask web container
	docker exec -it $(API_CONTAINER) /bin/bash

ssh-db: ## Open bash shell in Postgres container
	docker exec -it $(DB_CONTAINER) /bin/bash

run: ## Run Flask app inside web container (attach)
	docker-compose exec api flask run --host=0.0.0.0 --port=5000

migrate: ## Generate a new migration script
	docker-compose exec api flask db migrate -m "Auto migration"

upgrade: ## Apply migrations to the database
	docker-compose exec api flask db upgrade

downgrade: ## Revert the last migration (careful!)
	docker-compose exec api flask db downgrade

migrate-upgrade: migrate upgrade ## Run migrate and then upgrade in sequence

migrate-init: ## Initialize migration scripts folder
	docker-compose exec api flask db init

test: ## Run pytest locally (assuming virtualenv activated)
	pytest -s