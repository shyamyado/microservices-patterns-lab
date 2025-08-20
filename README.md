
# Microservices Patterns Lab

A **practice environment** for learning microservices patterns using **Python + uv + Docker**.

> **Current State:** Only the infrastructure layer is set up. Microservices will be added later.

---

## Prerequisites

1. **Docker Desktop** (with WSL2 integration if on Windows)
2. **Python 3.11+** (optional for later microservices)
3. **uv** (optional for local service testing later)

---

## Project Structure

High-level folder structure:
```
microservices-patterns-lab/
├── infra/         # Docker Compose, .env, Makefile
├── gateway/       # NGINX API Gateway
├── services/      # Microservices (FastAPI + uv; to be added)
├── patterns/      # Microservices patterns practice examples
└── scripts/       # Utility scripts (DB init, seed, cleanup)

```

---

## Infrastructure Setup

### Configure Services

Edit `infra/.env` to enable/disable services:

```env
ENABLE_POSTGRES=true
ENABLE_REDIS=false
ENABLE_RABBITMQ=true
ENABLE_GATEWAY=false
```

* `true` → service starts automatically with `make up`
* `false` → service does not start automatically but can be started manually

---

### Start Infrastructure

```bash
cd infra

# Start all enabled services
make up
```

**Enabled services will start based on `.env`.**

---

### Stop Infrastructure

```bash
make down
```

* Stops all running services
* Removes volumes for a clean start

---

### Start Services Manually

```bash
# Start Postgres only
make postgres

# Start Redis only
make redis

# Start RabbitMQ only
make rabbitmq

# Start NGINX gateway
make nginx
```

---

## Verify Infrastructure

* **Postgres:** `localhost:5432`
* **RabbitMQ Management UI:** `http://localhost:15672` (guest / guest)
* **NGINX API Gateway:** `http://localhost`

> Note: NGINX is running but no microservices exist yet, so requests may return “502 Bad Gateway”.

---

## Connect Tools

**pgAdmin (Windows or Mac)**:

* Host: `localhost`
* Port: `5432`
* DB: `demo`
* User: `user`
* Password: `pass`

**RabbitMQ UI**:

* URL: `http://localhost:15672`
* Login: `guest / guest`

---

## Notes

* The infrastructure is **modular**: you can start only the services you need.
* `.env` allows selective resource usage to save CPU/RAM.
* NGINX is ready as an API Gateway for future microservices.
* Microservices and pattern examples will be added in the `services/` and `patterns/` folders.

