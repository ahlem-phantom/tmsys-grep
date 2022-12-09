from pydoc import cli
import uuid
import datetime
from src.app import db
from src.models import Driver
from flask import jsonify, make_response
import jwt 
import os 
from datetime import datetime, timedelta, date
import json


#Create user
def create_driver(body):
        driver_firstname = body['driver_firstname'];
        driver_lastname = body['driver_lastname'];
        driver_phone = body['driver_phone'];
        driver_email = body['driver_email'];
        driver_licence = body['driver_licence'];
        data = Driver(driver_firstname, driver_lastname, driver_phone, driver_email, driver_licence)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True 
        })

#Get driver
def get_driver(id):
    driver = Driver.query.filter_by(id=id).first()
    if not driver:
        return jsonify({'driver' : 'No Driver found!', 'status' : False})
    driver_data = {}
    driver_data['id'] = driver.id
    driver_data['driver_firstname'] = driver.driver_firstname
    driver_data['driver_lastname'] = driver.driver_lastname
    driver_data['driver_phone'] = driver.driver_phone 
    driver_data['driver_status'] = json.dumps(driver.driver_status, default=lambda x: x.name)
    driver_data['driver_email'] = driver.driver_email
    driver_data['driver_lat'] = driver.driver_lat
    driver_data['driver_lng'] = driver.driver_lng
    driver_data['driver_licence'] = driver.driver_licence
    return jsonify({'driver' : driver_data, 'success' : True})

#Get drivers
def get_drivers():
    drivers = Driver.query.all()
    output = []
    for driver in drivers :
        drivers_data = {}
        drivers_data['id'] = driver.id
        drivers_data['driver_firstname'] = driver.driver_firstname
        drivers_data['driver_lastname'] = driver.driver_lastname
        drivers_data['driver_phone'] = driver.driver_phone 
        drivers_data['driver_status'] = json.dumps(driver.driver_status, default=lambda x: x.name)
        drivers_data['driver_email'] = driver.driver_email
        drivers_data['driver_lat'] = driver.driver_lat
        drivers_data['driver_lng'] = driver.driver_lng
        drivers_data['driver_licence'] = driver.driver_licence
        output.append(drivers_data)
    return jsonify({'drivers' : output, 'success' : True})

#Delete driver
def delete_driver(id):
    driver = Driver.query.filter_by(id=id).first()
    if not driver:
        return jsonify({'message' : 'No driver found!', 'success' : False})      
    db.session.delete(driver)
    db.session.commit()
    return jsonify({ 
            'status': 'Driver has been deleted successfuly !',
            'errors': [],
            'data' : {       
             }      
    })