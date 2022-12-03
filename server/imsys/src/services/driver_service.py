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
        driver_lat = body['driver_lat'];
        driver_lng = body['driver_lng'];
        driver_licence = body['driver_licence'];
        data = Driver(driver_firstname, driver_lastname, driver_phone, driver_email, driver_lat, driver_lng, driver_licence)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True 
        })

