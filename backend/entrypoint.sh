#!/bin/sh

# Collect static files
echo "---- Collect static files ----"
./manage.py collectstatic --noinput

# Apply database migrations
echo "---- Apply database migrations ----"
./manage.py migrate

#Create django superuser admin qweqwe111, create site name if not created, populate DB
echo "---- Init project ----"
./manage.py project_init

exec "$@"