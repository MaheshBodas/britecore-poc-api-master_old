#!/bin/bash

echo "==> Removing all data from the database..."
python manage.py flush --noinput

echo "==> Loading user fixtures..."
python manage.py loaddata riskapi/fixtures/users.json

echo "==> Loading riskapi fixtures..."
python manage.py loaddata riskapi/fixtures/riskapi.json

echo "==> Done!"
