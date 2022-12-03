from flask import Flask, jsonify
from .models import db
from .api import blueprint as us_blueprint
import os

def create_app(env_name):
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    db.init_app(app)
    app.register_blueprint(us_blueprint)
   
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({'message': 'lol xd'})

    return app
