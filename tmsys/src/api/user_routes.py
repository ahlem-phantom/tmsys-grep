from flask import request
from ..services.user_service import login, new_user, delete_user, get_users, get_user, update_user
from ..shared.authentication import token_required
from flask import Blueprint

user_api = Blueprint('user', __name__)


@token_required
@user_api.route('/login', methods=['POST'])
def Login():
      data = request.json
      return login(data)

@user_api.route('/add-user', methods=['POST'])
def addUser():
    data = request.json
    return new_user(data)

@user_api.route('/delete-user/<int:id>', methods=['POST'])
def deleteUser(id):
    return delete_user(id)


@user_api.route('/list-users', methods=['GET'])
def getUsers():
    return get_users()

@user_api.route('/get-user/<int:id>', methods=['GET'])
def getUser(id):
    return get_user(id)

@user_api.route('/update-user/<int:id>', methods=['POST'])
def editUser(id):
    data = request.json
    return update_user(id,data)