set -e

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=password1561
export DJANGO_SUPERUSER_EMAIL=nomail@email.com

python ./drf_jwt_backend/manage.py migrate

python ./drf_jwt_backend/manage.py createsuperuser --noinput

python ./drf_jwt_backend/manage.py runserver 0.0.0.0:8000