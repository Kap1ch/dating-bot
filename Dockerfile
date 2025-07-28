FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:0.8.2 /uv /uvx /bin/


WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY . .

RUN chmod +x start.sh
