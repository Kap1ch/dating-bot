#!/bin/sh

echo "🔄 Running migrations..."
alembic revision --autogenerate -m "Migration description"
alembic upgrade head

echo "🚀 Starting Bot..."
python main.py