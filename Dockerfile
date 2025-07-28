FROM python:3.13

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv pip install --system --no-deps

COPY . .

RUN chmod +x start.sh