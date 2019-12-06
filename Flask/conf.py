from app import app
import psycopg2
from psycopg2 import pool
import os,secrets,base64

app.config.update(
    SECRET_KEY=secrets.token_urlsafe(16),
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_NAME='FlaskAPI',
    WTF_CSRF_TIME_LIMIT=None,
    postgreSQL_pool= psycopg2.pool.SimpleConnectionPool(
        1,
        20,
        user = "postgres",
        password = "root",
        host = "127.0.0.1",
        port = "5432",
        database = "flaskDB"
    ),
)