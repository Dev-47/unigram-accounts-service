docker-compose build
docker-compose run --rm api python manage.py makemigrations
docker-compose run --rm api python manage.py migrate
