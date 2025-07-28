FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:0.8.2 /uv /uvx /bin/

ADD . /app

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"\
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

RUN uv sync --locked

RUN chmod +x start.sh
