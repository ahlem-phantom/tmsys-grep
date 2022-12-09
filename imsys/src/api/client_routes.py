from flask import request
from flask_restx import Resource
from ..services.client_service import create_client, get_clients, delete_client, update_client
from flask import Blueprint

client_api = Blueprint('client', __name__)

@client_api.route('/add-client', methods=['POST'])
def addClient():
    data = request.json
    return create_client(data)


@client_api.route('/all-clients', methods=['GET'])
def getClients():
    return get_clients()

@client_api.route('/delete-client/<int:id>', methods=['DELETE'])
def deleteClient(id):
    return delete_client(id)


@client_api.route('/update-user/<int:id>', methods=['DELETE'])
def updateClient(id,data):
    return update_client(id,data)
