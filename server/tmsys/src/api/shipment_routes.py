from flask import request
from ..services.shipment_service import create_shipment, assign_shipment
from flask import Blueprint

shipment_api = Blueprint('shipment', __name__)

@shipment_api.route('/add-shipment', methods=['POST'])
def addShipment():
    data = request.json
    return create_shipment(data)

@shipment_api.route('/assign-shipment', methods=['GET'])
def assignShipment():
    data = request.json
    return assign_shipment()