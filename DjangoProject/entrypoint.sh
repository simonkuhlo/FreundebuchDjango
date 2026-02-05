#!/usr/bin/env bash

python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput

# Gunicorn with structured logging to stdout
exec python -m gunicorn \
  --bind 0.0.0.0:8000 \
  --workers $(expr $(nproc) \* 2 + 1) \
  --worker-class uvicorn.workers.UvicornWorker \
  --log-level info \
  --access-logfile - \
  --error-logfile - \
  BlumeMain.wsgi:application
