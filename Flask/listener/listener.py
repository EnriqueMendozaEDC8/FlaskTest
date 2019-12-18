from app import app
from flask import session,redirect,url_for,request,jsonify,render_template
import model.model as model
import os,secrets,base64,json

#   DO: Return key and user from request
#   @param 
#   @return json user,key
def uncryptedpKey(encryptedkey):
    decodeKeyAndUser = base64.b64decode(request.headers.get('Key')).decode("utf-8")
    splittedCode = decodeKeyAndUser.split('USER:')
    return {'user':splittedCode[1],'key':base64.b64decode(splittedCode[0]).decode("utf-8")}

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
        jsonKey = uncryptedpKey(request.headers.get('Key'))
        if(jsonKey['key'] == app.secret_key):
            response = model.get_users()
            return jsonify({'data':response})
        return jsonify({'error':'not is the same key'})
    except:
        return jsonify({'error':'we have some error'})

#   DO: Return One user from database
#   @param Number id
#   @return json data
@app.route("/postuser",methods = ['POST'])
def postuser():
    try:
        jsonKey = uncryptedpKey(request.headers.get('Key'))
        if(jsonKey['key'] == app.secret_key):
            idUser = request.json.get('id')
            response = model.get_one_user(idUser)
            return jsonify({'data':response})
        return jsonify({'error':'not is the same key'})
    except:
        return jsonify({'error':'we have some error'})

#   DO: Insert a new user in database
#   @param Text name, Date birthdate, Text job
#   @return json data
@app.route("/putuser", methods=['PUT'])
def putuser():
    try:
        jsonKey = uncryptedpKey(request.headers.get('Key'))
        if(jsonKey['key'] == app.secret_key):
            name = request.json.get('name')
            birthdate = request.json.get('birthdate')
            job = request.json.get('job')
            response = model.insert_user(name,birthdate,job)
            return jsonify({'data':response})
        return jsonify({'error':'not is the same key'})
    except:
        return jsonify({'error':'we have some error'})

#   DO: Delete user from database
#   @param Number id
#   @return json data
@app.route("/deleteuser", methods=['DELETE'])
def deleteuser():
    try:
        jsonKey = uncryptedpKey(request.headers.get('Key'))
        if(jsonKey['key'] == app.secret_key):
            idUser = request.json.get('id')
            response = model.delete_user(idUser)
            return jsonify({'data':response})
        return jsonify({'error':'not is the same key'})
    except:
        return jsonify({'error':'we have some error'})

#   DO: Return secretkey
#   @param
#   @return json data
@app.route("/getsecretkey", methods=['POST'])
def getsecretkey():
    #session['user'] = 'enrique'
    #session['pws'] = 'flask'
    #session['key'] = base64.b64encode(app.secret_key.encode('ascii')).decode("utf-8")
    return jsonify({'key':base64.b64encode(app.secret_key.encode('ascii')).decode("utf-8")})
    
#   DO: Return responsecode
#   @param
#   @return json data
@app.route("/getresponsekey", methods=['POST'])
def getresponsekey():
    key=request.json.get('key')+'USER:'+request.json.get('user')
    return jsonify({'key':base64.b64encode(key.encode('ascii')).decode("utf-8")})