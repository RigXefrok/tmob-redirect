<!-- First you need to create the .env file with: -->
<!-- #MYSQL ENVIROMENT -->

MYSQL_ROOT_PASSWORD=''\
MYSQL_DATABASE=''\
MYSQL_USER=''\
MYSQL_PASSWORD=''\
MYSQL_PORT=3306\
MYSQL_HOST=127.0.0.1

<!-- #MEMCACHED ENVIROMENT -->

MEMCACHED_HOST='127.0.0.1'\
MEMCACHED_PORT=11211

<!-- #DJANGO SETTINGS ENVIROMENT -->

SECURITY_KEY='ultra security key'\
DEBUG=True\
ALLOWED_HOSTS="\*"

<!-- Create virtualenv -->

pip install virtualenv virtualenv venv --python='/usr/bin/3.8'

<!-- Install dependencies -->

pip install requirements.txt

<!-- Set the databases and cache containers -->

docker compose up

<!-- Updates the cache with databases active redirects -->

py manage.py set_memcached

<!-- Serve application -->

py ./manage.py runserver
