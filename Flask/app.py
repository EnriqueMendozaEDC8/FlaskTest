#Import Libraries
from flask import Flask
import psycopg2
from psycopg2 import pool
from flask_cors import CORS
import os

#Start Flask
app = Flask(__name__)
CORS(app)

#Custom imports
import conf
from listener.listener import *

#Run App
if __name__ == '__main__':
    app.run(debug=True)