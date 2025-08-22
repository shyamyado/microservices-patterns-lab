FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy service code
COPY . .

# Copy patterns into container
COPY ../../patterns /app/patterns

# Install dependencies
RUN uv sync --frozen --no-cache

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]
