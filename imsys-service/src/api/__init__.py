from flask_restx import Api
from flask import Blueprint
from src.api.user_routes import api as user_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='FLASK TMS RESTFUL API',
    version='1.0',
    description='Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc'
)

api_extension.add_namespace(user_ns, path='/user')

