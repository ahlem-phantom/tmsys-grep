from flask import request, jsonify
from ..services.shipment_service import create_shipment, assign_shipment
#, get_shipment, get_currentShipment, get_number
from flask import Blueprint
from ..models import Shipment
from ..services.truck_service import get_truck
from ..services.order_service import get_order
from ..services.driver_service import get_driver
import json
from sqlalchemy import asc

shipment_api = Blueprint('shipment', __name__)

@shipment_api.route('/add-shipment', methods=['POST'])
def addShipment():
    data = request.json
    return create_shipment(data)

@shipment_api.route('/assign-shipment', methods=['GET'])
def assignShipment():
    return assign_shipment()

@shipment_api.route('/get-shipments', methods=['GET'])
def get_shipments():
    #shipments = Shipment.query.filter_by(shipment_status ='ON_ROUTE').order_by(asc(Shipment.shipment_id))
    shipments = Shipment.query.all()
    output = []

    for shipment in shipments:
        shipment_data = {}
        shipment_data['shipment_id'] = shipment.shipment_id
        shipment_data['shipment_seq'] = shipment.shipment_seq
        shipment_data['shipment_status'] = json.dumps(shipment.shipment_status, default=lambda x: x.name)
        shipment_data['truck'] = json.loads(get_truck(shipment.truck_id).data)['truck']
        shipment_data['order'] = json.loads(get_order(shipment.order_id).data)['order']
        shipment_data['driver'] =  json.loads(get_driver(json.loads(get_truck(shipment.truck_id).data)['truck']["driver_id"]).data)['driver']
        output.append(shipment_data)
    return jsonify({'shipments' : output, 'success' : True})

'''
@shipment_api.route('/get-shipment/<int:id>', methods=['GET'])
def getShipment(id):
    return get_shipment(id)

@shipment_api.route('/get-currentshipment/<int:id>', methods=['GET'])
def getCurrentShipment(id):
    return get_currentShipment(id)

@shipment_api.route('/get-number', methods=['GET'])
def getNumber():
    return get_number()
'''