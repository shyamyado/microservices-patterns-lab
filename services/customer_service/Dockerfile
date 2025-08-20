FROM python:3.11-slim

WORKDIR /app

# Install uv globally
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies (reproducible via lockfile)
RUN uv sync --frozen --no-cache

# Copy app source code
COPY . .

# Run service with uv
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
