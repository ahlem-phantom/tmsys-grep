from flask import request
from ..util.dto import User_1 ,User_2 , User_3
from flask_restx import Resource
from ..services.user_service import login, new_user, delete_user, get_users, get_user, update_user
from ..shared.authentication import token_required

api = User_1.api
_user2 = User_2.user
_user3 = User_3.user

@token_required
@api.route('/login')
class UserLogin(Resource):

    @api.doc('User Authentication')
    @api.response(201, 'User successfully authenticated !')
    @api.expect(_user2, validate=True)
    def post(self):
        data = request.json
        return login(data)

@api.route('/add-user')
class UserAdd(Resource):

    @api.doc('User Registration')
    @api.response(201, 'User successfully created !')
    @api.expect(_user3, validate=True)
    def post(self):
        data = request.json
        return new_user(data)

@api.route('/delete-user/<int:id>')
class UserDelete(Resource):
    @api.doc('User DELETE')
    @api.doc(params={'x-access-token': {'in': 'header', 'description': 'An authorization token'}})
    @api.response(201, 'User successfully deleted !')
    def delete(self,id):
        return delete_user(id)


@api.route('/list-users')
class UserList(Resource):
    @api.doc('Users GET')
    @api.doc(params={'x-access-token': {'in': 'header', 'description': 'An authorization token'}})
    @api.response(201, 'User successfully listed !')
    def get(self):
        return get_users()

@api.route('/get-user/<int:id>')
class UserById(Resource):
    @api.doc('Get User by id')
    @api.doc(params={'x-access-token': {'in': 'header', 'description': 'An authorization token'}})
    @api.response(201, 'success !')
    def get(self,id):
        return get_user(id)

@api.route('/update-user/<int:id>')
class UserUpdate(Resource):
    @api.doc('Update User')
    @api.doc(params={'x-access-token': {'in': 'header', 'description': 'An authorization token'}})
    @api.response(201, 'User updated successfully !')
    def put(self,id):
        data = request.json
        return update_user(id,data)