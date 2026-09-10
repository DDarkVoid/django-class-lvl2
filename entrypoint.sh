#!/usr/bin/env sh
set -e

echo "Waiting for PostgreSQL to start..."

python << END
import socket
import time
import os

host = os.getenv('POSTGRES_HOST', 'db')
port = int(os.getenv('POSTGRES_PORT', 5432))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect((host, port))
        s.close()
        break
    except socket.error:
        time.sleep(0.5)
END

echo "PostgreSQL started successfully."

python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000