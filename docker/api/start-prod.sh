#!/bin/bash

echo "Waiting for db"

while ! nc -z mongo 27017; do
  sleep 0.1
done

echo "DB started"

exec "$@"

gunicorn techposts.app.main:app --bind 0.0.0.0:80 --workers 1 --worker-class uvicorn.workers.UvicornWorker
