import uuid
import datetime
from src.app import db
from src.models import User
from flask import jsonify, make_response
import jwt 
import os 
from datetime import datetime, timedelta, date
from  werkzeug.security import generate_password_hash, check_password_hash
from src.shared.authentication import token_required
import json
    
#User Authentication
def login(body):

    if not body['username'] or not body['password'] or not body:
     return jsonify({ 
            'status': False,
            'errors':  [
               {
                  "errnumber": "c7ab4814cdf7c88e991490af28bd2c9c",
                  "errordesc": "Username and password required !",
                  "errofield": "username",
                  "errolevel": "UNAUTHORISED",
                  "edatetime": date.today()
               }
              ],
            'data' : []
           
        })
    username = body['username']
    password = body['password']
    user = User.query.filter_by(username=username).first() 
    if not user:
        # returns 401 if user does not exist
        return jsonify({ 
            'status': False,
            'errors':  [
               {
                  "errnumber": "c7ab4814cdf7c88e991490af28bd2c9c",
                  "errordesc": "User does not exist !",
                  "errofield": "username",
                  "errolevel": "UNAUTHORISED",
                  "edatetime": date.today()
               }
              ],
            'data' : []
           
        })
    #password check
    if check_password_hash(user.password, password):
        token = jwt.encode({
            'token': user.token,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, os.environ['SECRET_KEY'], "HS256")

        return jsonify({ 
            'status': True,
            'errors': [],
            'data' : {
                  'sessionRequest': [
                   { 
                     'token': token.decode()
                   }
                   ],
                   'menu': [
                   {
                       'username': username,
                       'password' : password
                   }
                   ]               
             }
           
        })
        
        
    return jsonify({ 
            'status': False,
            "errors": [
               {
                  "errnumber": "c7ab4814cdf7c88e991490af28bd2c9c",
                  "errordesc": "password mismatch!",
                  "errofield": "password",
                  "errolevel": "ERROR",
                  "edatetime": date.today()
               }
              ],
             'data': []          
        })




#Create user
def new_user(body):
        username = body['username']
        password = body['password']
        role = body['role']
        token = str(uuid.uuid4())
        hashpwd = generate_password_hash(password)
        data = User( username, hashpwd, role, token)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True,
            'errors': [],
            'data' : {
                  'sessionRequest': [
                   { 
                     'token': token
                   }
                   ],
                   'menu': [
                   {
                       'username': username,
                       'password' : password
                   }
                   ]               
             }
           
        })
    

#Delete user
@token_required 
def delete_user(current_user,id):

    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message' : 'No user found!', 'success' : False})
        
    db.session.delete(user)
    db.session.commit()
    return jsonify({ 
            'status': 'User has been deleted successfuly !',
            'errors': [],
            'data' : {
                 
             }
           
        })

#Get users   
@token_required
def get_users(current_user):

    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['role'] = json.dumps(user.role, default=lambda x: x.name)
        user_data['token'] = user.token
        output.append(user_data)
    return jsonify({'users' : output, 'success' : True})

#Get users by id
@token_required
def get_user(current_user,id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message' : 'No user found!', 'success' : False})
    user_data = {}
    user_data['id'] = user.id
    user_data['username'] = user.username
    user_data['password'] = user.password
    user_data['role'] = json.dumps(user.role, default=lambda x: x.name)
    user_data['token'] = user.token
    return jsonify({'user' : user_data, 'success' : True})


#Update user
@token_required
def update_user(current_user,id,body):
    user = User.query.get(id)
    if body.get('username', user.username) : 
        user.username = body.get('username', user.username)
        
    if body.get('password', user.password) : 
        hashpwd = generate_password_hash(body.get('password', user.password))
        user.password = hashpwd

    if body.get('role', user.role) : 
        user.role = body.get('role', user.role)
    db.session.commit()
    return jsonify({ 
            'status': True,
            'errors': [],
            'data' : {
                  'sessionRequest': [
                   { 
                     'token': user.token
                   }
                   ],
                   'menu': [
                   {
                       'username': user.username,
                       'password' : user.password
                   }
                   ]               
             }
           
        })

