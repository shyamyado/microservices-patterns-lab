# Include environment variables
include .env

# Start only services enabled in .env
up:
	@echo "Starting enabled services..."
	@for profile in $$(awk -F= '/^ENABLE_/ && $$2=="true" {print tolower(substr($$1,8))}' .env); do \
		echo "Starting $$profile..."; \
		docker compose -f infrastructure.yml --profile $$profile up -d; \
	done
	@echo "All enabled services started."

# Stop everything
down:
	docker compose -f infrastructure.yml down -v

# Manual start commands
postgres:
	docker compose -f infrastructure.yml --profile postgres up -d

redis:
	docker compose -f infrastructure.yml --profile redis up -d

rabbitmq:
	docker compose -f infrastructure.yml --profile rabbitmq up -d

nginx:
	docker compose -f infrastructure.yml --profile gateway up -d
