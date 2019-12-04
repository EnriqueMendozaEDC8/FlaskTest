from app import app
from flask import session,redirect,url_for,request,jsonify,render_template
import model.model as model
#Import Model
#import models.indexModel as indexModel

#   DO: render template with info
#   @param 
#   @return render template
@app.route("/")
def index():
    return render_template('index.html')

#   DO: return all users in database
#   @param 
#   @return json data
@app.route("/getuser",methods = ['GET'])
def getuser():
    try:
        response = model.get_users()
        return jsonify({'data':response})
    except:
        return jsonify({'error':'we have some error'})

#   DO: Return One user from database
#   @param Number id
#   @return json data
@app.route("/postuser",methods = ['POST'])
def postuser():
    try:
        print(request.json)
        idUser = request.json.get('id')
        response = model.get_one_user(idUser)
        return jsonify({'data':response})
    except:
        return jsonify({'error':'we have some error'})

#   DO: Insert a new user in database
#   @param Text name, Date birthdate, Text job
#   @return json data
@app.route("/putuser", methods=['PUT'])
def putuser():
    try:
        name = request.json.get('name')
        birthdate = request.json.get('birthdate')
        job = request.json.get('job')
        response = model.insert_user(name,birthdate,job)
        return jsonify({'data':response})
    except:
        return jsonify({'error':'we have some error'})

#   DO: Delete user from database
#   @param Number id
#   @return json data
@app.route("/deleteuser", methods=['DELETE'])
def deleteuser():
    try:
        idUser = request.json.get('id')
        response = model.delete_user(idUser)
        return jsonify({'data':response})
    except:
        return jsonify({'error':'we have some error'})
