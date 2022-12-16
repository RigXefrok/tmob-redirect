# Create .env file which includes:

MYSQL_ROOT_PASSWORD=""\
MYSQL_DATABASE=""\
MYSQL_USER=""\
MYSQL_PASSWORD=""\
MYSQL_PORT=3306\
MYSQL_HOST="127.0.0.1"

MEMCACHED_HOST="127.0.0.1"\
MEMCACHED_PORT=11211

SECURITY_KEY="ultra security key"\
DEBUG=True\
ALLOWED_HOSTS="\*"

# Create virtualenv with python 3.8

pip install virtualenv virtualenv venv --python="/usr/bin/3.8"

# Install dependencies

pip install requirements.txt

# Set the database and cache containers

docker compose up

# Run application 😀

py ./manage.py runserver

# Load previous actives redirects

py ./manage.py set_memcached
