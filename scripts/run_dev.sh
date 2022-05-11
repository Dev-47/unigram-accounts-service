docker-compose build api
docker-compose run --rm -p 1000:8000 api python manage.py runserver 0.0.0.0:8000
