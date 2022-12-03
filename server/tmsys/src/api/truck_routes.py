from flask import request
from ..services.truck_service import create_truck , get_trucks, get_truck
from flask import Blueprint

truck_api = Blueprint('truck', __name__)

@truck_api.route('/add-truck', methods=['POST'])
def addTruck():
    data = request.json
    return create_truck(data)


@truck_api.route('/all-trucks', methods=['GET'])
def getTrucks():
    return get_trucks()


@truck_api.route('/get-truck/<int:id>', methods=['GET'])
def getTruck(id):
    return get_truck(id)
