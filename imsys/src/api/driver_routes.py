from flask import request
from ..services.driver_service import create_driver
from flask import Blueprint

driver_api = Blueprint('driver', __name__)

@driver_api.route('/add-driver', methods=['POST'])
def addDriver():
    data = request.json
    return create_driver(data)