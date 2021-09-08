#!/usr/bin/env bash


python manage.py makemigrations
python manage.py migrate
# python manage.py loaddata ./api/fixtures/users.json
# python manage.py loaddata ./api/fixtures/address.json
# python manage.py loaddata ./api/fixtures/ranks.json
# python manage.py loaddata ./api/fixtures/sites.json
# python manage.py loaddata ./api/fixtures/articles.json
python manage.py runserver 0.0.0.0:8666