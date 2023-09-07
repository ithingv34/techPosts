#!/bin/bash

echo "Waiting for db"

while ! nc -z mongo 27017; do
  sleep 0.1
done

echo "DB started"

exec "$@"

uvicorn techposts.app.main:app --host 0.0.0.0 --port 80 --workers 1
