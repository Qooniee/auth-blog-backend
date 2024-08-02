#!/usr/bin/env bash
# exit on error
cd backend
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py superuser
