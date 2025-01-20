#!/usr/bin/env bash

# Exit on error
set -o errexit

# Upgrade pip and install Python packages
python -m pip install --upgrade pip
pip install virtualenv
python -m virtualenv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
pip install gunicorn

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser if needed (optional)
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Deactivate virtual environment
deactivate 