#Import Libraries
from flask import Flask
import psycopg2
from psycopg2 import pool
from flask_cors import CORS

import os

#Start Flask
app = Flask(__name__)
CORS(app)
app.secret_key = 'flask'
app.config['postgreSQL_pool'] = psycopg2.pool.SimpleConnectionPool(
    1,
    20,
    user = "XXXXXXX",
    password = "XXXXXXXXX",
    host = "db-postgresql-nyc1-19058-do-user-6568752-0.db.ondigitalocean.com",
    port = "XXXXXX",
    database = "flaskDB"
)
from listener.listener import *

#Run App
if __name__ == '__main__':
    app.run(debug=True)