import enum
from flask_restx import Namespace, fields

class UserRole(enum.Enum):
    Client = 'Client',
    Manager = 'Manager',
    Admin = 'Admin',
    Driver = 'Driver'

class User_1:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user username'),
        'role': fields.String(attribute=lambda x: str(UserRole(x.FieldContainingEnum).name)),
        'token': fields.String(required=True, description='user role'),
    })

class User_2:
    api = Namespace('user2', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user username')
    })

class User_3:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user username'),
        'role': fields.String(attribute=lambda x: str(UserRole(x.FieldContainingEnum).name)),

    })