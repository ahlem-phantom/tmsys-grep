from flask import request
from ..services.driver_service import create_driver, get_driver, get_drivers, delete_driver
from flask import Blueprint

driver_api = Blueprint('driver', __name__)

@driver_api.route('/add-driver', methods=['POST'])
def addDriver():
    data = request.json
    return create_driver(data)

@driver_api.route('/get-driver/<int:id>', methods=['GET'])
def getTruck(id):
    return get_driver(id)

@driver_api.route('/all-drivers', methods=['GET'])
def getTrucks():
    return get_drivers()

@driver_api.route('/delete-driver/<int:id>', methods=['DELETE'])
def deleteDriver(id):
    return delete_driver(id)