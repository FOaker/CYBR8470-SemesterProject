python manage.py makemigrations&&
python manage.py migrate&&
uwsgi --ini /var/www/html/blog/uwsgi.ini
