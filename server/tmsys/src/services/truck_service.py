from pydoc import cli
import uuid
import datetime
from src.app import db
from src.models import Truck
from flask import jsonify, make_response
import jwt 
import os 
from datetime import datetime, timedelta, date
import json


#Create truck
def create_truck(body):
        truck_name = body['truck_name'];
        truck_type = body['truck_type'];
        truck_plate = body['truck_plate'];
        truck_year = body['truck_year'];
        truck_model = body['truck_model'];
        truck_capacity = body['truck_capacity'];
        truck_size = body['truck_size'];
        truck_engine = body['truck_engine'];
        truck_color = body['truck_color'];
        #driver_id = body['driver_id'];
        data = Truck( truck_name,truck_type,truck_plate, truck_year, truck_model, truck_capacity, truck_size, truck_engine, truck_color)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True 
        })

#Get trucks
def get_trucks():
    trucks = Truck.query.all()
    output = []
    for truck in trucks:
        truck_data = {}
        truck_data['truck_id'] = truck.truck_id
        truck_data['truck_name'] = truck.truck_name 
        truck_data['truck_plate'] = truck.truck_plate 
        truck_data['truck_year'] = truck.truck_year 
        truck_data['truck_model'] = truck.truck_model 
        truck_data['truck_capacity'] = truck.truck_capacity 
        truck_data['truck_size'] = truck.truck_size 
        truck_data['truck_engine'] = truck.truck_engine
        truck_data['truck_color'] = truck.truck_color 
        truck_data['truck_type'] = json.dumps(truck.truck_type, default=lambda x: x.name)
        truck_data['truck_status'] = json.dumps(truck.truck_status, default=lambda x: x.name)
        truck_data['created_at'] = truck.created_at
        truck_data['driver_id'] = truck.driver_id
        output.append(truck_data)
    return jsonify({'trucks' : output, 'success' : True})

#Get truck by id
def get_truck(id):
    truck = Truck.query.filter_by(truck_id=id).first()
    if not truck:
        return jsonify({'message' : 'No truck found!', 'success' : False})
    truck_data = {}
    truck_data['truck_id'] = truck.truck_id
    truck_data['truck_name'] = truck.truck_name 
    truck_data['truck_plate'] = truck.truck_plate 
    truck_data['truck_year'] = truck.truck_year 
    truck_data['truck_model'] = truck.truck_model 
    truck_data['truck_capacity'] = truck.truck_capacity 
    truck_data['truck_size'] = truck.truck_size 
    truck_data['truck_engine'] = truck.truck_engine
    truck_data['truck_color'] = truck.truck_color 
    truck_data['truck_status'] = json.dumps(truck.truck_status, default=lambda x: x.name)
    truck_data['truck_type'] = json.dumps(truck.truck_type, default=lambda x: x.name)
    truck_data['created_at'] = truck.created_at
    truck_data['driver_id'] = truck.driver_id
    return jsonify({'truck' : truck_data, 'success' : True})

#Count total number of available truck
def get_length():
    trucks = Truck.query.with_entities(Truck.truck_id)
    output = []
    for truck in trucks:
        truck_data = {}
        truck_data['truck_id'] = truck.truck_id
        output.append(truck_data)
    return jsonify({'truck' : output, 'success' : True})

#Assign driver to truck
def assign_driver(id,body):
    truck = Truck.query.get(id)
    if body.get('driver_id', truck.driver_id) : 
        truck.driver_id = body.get('driver_id', truck.driver_id)
        db.session.commit()
    return jsonify({
            'status': True 
        })