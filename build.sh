echo '#!/usr/bin/env bash

# Exit on error
set -o errexit

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate' > build.sh