from app import app
from flask import jsonify,g
import json

def get_db():
    if 'db' not in g:
        g.db = app.config['postgreSQL_pool'].getconn()
    return g.db

@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['postgreSQL_pool'].putconn(db)

def get_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("select idperson,nombre,fechanacimiento,puesto from personas;")
    result = cursor.fetchall()
    cursor.close()
    return result

def get_one_user(idUser):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("select nombre,fechanacimiento,puesto from personas where idperson = %s;",(str(idUser)))
    result = cursor.fetchall()
    cursor.close()
    return result

def insert_user(name,birthdate,job):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("insert into personas(nombre,fechanacimiento,puesto) values(%s,%s,%s);",(str(name),str(birthdate),str(job)))
    db.commit()
    cursor.close()
    return 'SUCCESSFUL'
    
def delete_user(idUser):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM personas where idperson = %s;",(str(idUser))) 
    db.commit()
    cursor.close()
    return 'SUCCESSFUL'