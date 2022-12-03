from src.models import User
from functools import wraps
from flask import request, jsonify, make_response
import jwt 
import os 


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'a valid token is missing'})
  
        try:
          # decoding the payload to fetch the stored details
           data = jwt.decode(token, os.environ['SECRET_KEY'],algorithms=["HS256"])
           current_user = User.query.filter_by(token=data['token']).first()
        except:
            return make_response(jsonify({
                'message' : 'Token is invalid !!'
            }), 401)
       
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs) 
    return decorated


'''
import uuid
import datetime
from ..models.user import User
from functools import wraps
import jwt
from flask import Flask, jsonify, request
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_tokens(username_input):

    user = User.query.filter_by(username=username_input).first()

    matchid = str(uuid.uuid4())

    token_content = {
        'public_id' : user.public_id,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'username' : user.username,
        'email' : user.email,
        'email_verified' : user.email_verified,
        'is_staff' : user.is_staff,
        'is_admin' : user.is_admin,
        'created_at' : str(user.created_at),
        'modified_at' : str(user.modified_at),
        'tokenmatchid' : matchid,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    refresh_token_content = {
        'public_id' : user.public_id,
        'username' : user.username,
        'email' : user.email,
        'refreshtokenmatchid' : matchid,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }

    token = jwt.encode(token_content, os.environ['SECRET_KEY'])
    refresh_token = jwt.encode(refresh_token_content, os.environ['SECRET_KEY'])

    list_of_tokens = [token, refresh_token]

    return list_of_tokens

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, os.environ['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()

        except jwt.ExpiredSignatureError:
            return jsonify({'message' : 'Token is expired!', 'expired' : True}), 403

        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

def send_conf_email(receiver_address, conf_link):
    mail_content = f Hello,
    Please click this link to verify your email: {conf_link}

    Team
    TheBaton
    
    sender_address = os.environ['SENDER_ADD']
    sender_pass = os.environ['SENDER_PASS']
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Confirm Email'

    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls() 
    session.login(sender_address, sender_pass)
    text = message.as_string()
    try:
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        return {'success': True}
        
    except:
        session.quit()
        return {'success' : False}
'''