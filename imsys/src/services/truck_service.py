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


#Create user
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
        driver_id = body['driver_id'];
        data = Truck( truck_name,truck_type,truck_plate, truck_year, truck_model, truck_capacity, truck_size, truck_engine, truck_color , driver_id)
        db.session.add(data)
        db.session.commit()
        return jsonify({ 
            'status': True 
        })

#Get clients
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
        truck_data['truck_status'] = json.dumps(truck.truck_status, default=lambda x: x.name)
        truck_data['created_at'] = truck.created_at
        output.append(truck_data)
    return jsonify({'trucks' : output, 'success' : True})

