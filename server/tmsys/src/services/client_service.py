from pydoc import cli
import uuid
import datetime
from src.app import db
from src.models import Client
from flask import jsonify, make_response
import jwt 
import os 
from datetime import datetime, timedelta, date
import json


#Create user
def create_client(body):
        company_name = body['company_name'];
        company_address = body['company_address'];
        company_phone = body['company_phone'];
        company_email = body['company_email'];
        data = Client(company_name,company_address,company_phone,company_email)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True 
        })

#Get clients
def get_clients():
    clients = Client.query.all()
    output = []
    for client in clients:
        client_data = {}
        client_data['client_id'] = client.client_id
        client_data['company_name'] = client.company_name
        client_data['company_phone'] = client.company_phone
        client_data['company_address'] = client.company_address
        client_data['company_email'] = client.company_email
        output.append(client_data)
    return jsonify({'clients' : output, 'success' : True})


#Delete clients
def delete_client(id):
    client = Client.query.filter_by(client_id=id).first()
    if not client:
        return jsonify({'message' : 'No user found!', 'success' : False})      
    db.session.delete(client)
    db.session.commit()
    return jsonify({ 
            'status': 'Client has been deleted successfuly !',
            'errors': [],
            'data' : {       
             }      
    })

def update_client(id,body):
    client = Client.query.get(id)
    if body.get('client_id', client.client_id) : 
        client.client_id = body.get('client_id', client.client_id)
        
    if body.get('company_name', client.company_name) : 
        client.company_name = body.get('company_name', client.company_name)

    if body.get('company_address', client.company_address) : 
        client.company_address = body.get('company_address', client.company_address)

    if body.get('company_email', client.company_email) : 
        client.company_email = body.get('company_email', client.company_email)

    if body.get('company_phone', client.company_phone) : 
        client.company_phone = body.get('company_phone', client.company_phone)

    db.session.commit()
    return jsonify({ 
            'status': True,
            'errors': [],
            'data' : {
                  'sessionRequest': [
                   { 
                     'token': " "
                   }
                   ],
                   'menu': [
                   {
                       
                   }
                   ]               
             }
           
        })

