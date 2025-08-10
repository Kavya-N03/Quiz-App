#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser if it doesn't exist (reads env vars set on Render)
python manage.py shell <<'PY'
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email or "", password)
        print("SUPERUSER_CREATED")
    else:
        print("SUPERUSER_ALREADY_EXISTS")
else:
    print("SUPERUSER_ENV_VARS_MISSING")
PY
