#!/bin/bash

set -euo pipefail
set -x

source /app/.venv/bin/activate

uv run python manage.py check --deploy &&
uv run python manage.py makemigrations &&
uv run python manage.py migrate &&
uv run python manage.py collectstatic --noinput &&
gunicorn house_prices.wsgi