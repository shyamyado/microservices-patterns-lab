# Include environment variables
include .env

# ------------------------------
# Helper: get enabled profiles from .env
# ------------------------------
ENABLED_PROFILES := $(shell awk -F= '/^ENABLE_/ && $$2=="true" {print tolower(substr($$1,8))}' .env)

# ------------------------------
# Start only enabled services
# ------------------------------
up:
	@echo "Starting enabled services..."
	@if [ -z "$(ENABLED_PROFILES)" ]; then \
		echo "No services enabled in .env"; \
	else \
		for profile in $(ENABLED_PROFILES); do \
			echo "Starting $$profile..."; \
			docker compose -f infrastructure.yml --profile $$profile up -d; \
		done \
	fi
	@echo "All enabled services started."

# ------------------------------
# Stop everything (all profiles)
# ------------------------------
# Stop all services by setting COMPOSE_PROFILES
down:
	@echo "Stopping all services..."
	@if [ -z "$(ENABLED_PROFILES)" ]; then \
		echo "No services enabled in .env, stopping all profiles manually..."; \
		docker compose -f infrastructure.yml \
			--profile rabbitmq \
			--profile gateway \
			--profile customer_service \
			--profile order_service \
			--profile payment_service \
			--profile inventory_service \
			down -v --remove-orphans; \
	else \
		for profile in $(ENABLED_PROFILES); do \
			echo "Stopping $$profile..."; \
			docker compose -f infrastructure.yml --profile $$profile down -v --remove-orphans; \
		done \
	fi
	@echo "All services stopped."


# ------------------------------
# Manual service start targets
# ------------------------------
postgres:
	@echo "Starting Postgres..."
	docker compose -f infrastructure.yml --profile postgres up -d

redis:
	@echo "Starting Redis..."
	docker compose -f infrastructure.yml --profile redis up -d

rabbitmq:
	@echo "Starting RabbitMQ..."
	docker compose -f infrastructure.yml --profile rabbitmq up -d

nginx:
	@echo "Starting Gateway..."
	docker compose -f infrastructure.yml --profile gateway up -d

# ------------------------------
# Convenience: stop single services
# ------------------------------
stop-postgres:
	docker compose -f infrastructure.yml --profile postgres down

stop-redis:
	docker compose -f infrastructure.yml --profile redis down

stop-rabbitmq:
	docker compose -f infrastructure.yml --profile rabbitmq down

stop-nginx:
	docker compose -f infrastructure.yml --profile gateway down
