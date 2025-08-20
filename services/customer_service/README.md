# Order Service

FastAPI microservice for managing orders, integrated with Postgres and RabbitMQ for a choreography saga pattern.

## Setup & Run

### 1. Create Virtual Environment
```bash
uv venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 2. Install Dependencies
```bash
uv sync
```
Installs `fastapi`, `uvicorn`, `pika`, `psycopg2-binary` from `pyproject.toml`.

### 3. Run the Service
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```
- API at `http://localhost:8002`
- `--reload` for development

## API Endpoints
| Method | Path             | Description         |
|--------|------------------|---------------------|
| GET    | `/orders`        | List all orders     |
| GET    | `/orders/{id}`   | Get order by ID     |
| POST   | `/orders`        | Create order        |
| PUT    | `/orders/{id}`   | Update order        |
| DELETE | `/orders/{id}`   | Delete order        |

## Docker
```bash
docker build -t order_service .
docker run -p 8002:8002 order_service
```
Use with `docker-compose` (`infra/infrastructure.yml`) for multi-service setup.

## Notes
- Uses `uv` for dependency management (`pyproject.toml`, `uv.lock`).
- Port `8002` aligns with Nginx (`infra/gateway/conf.d/default.conf`) and `infrastructure.yml`.
- Connects to `orderdb` (Postgres) and RabbitMQ for saga events (e.g., `order.requested`, `customer.validated`, `payment.processed`, `inventory.reserved`).