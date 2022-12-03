import os
from src.app import create_app
from flask_migrate import Migrate
from src.models import db
from flask_cors import CORS
import sys
from src.api.client_routes import client_api
from src.api.truck_routes import truck_api
from src.api.driver_routes import driver_api
from src.api.order_routes import order_api
from src.api.shipment_routes import shipment_api
from src.api.user_routes import user_api


env_name = os.environ['FLASK_ENV']
host = sys.argv[1] if sys.argv[1:] else "127.0.0.1"

app = create_app(env_name)
app.register_blueprint(user_api, url_prefix='/api/v1/users')
app.register_blueprint(client_api, url_prefix='/api/v1/clients')
app.register_blueprint(truck_api, url_prefix='/api/v1/trucks')
app.register_blueprint(driver_api, url_prefix='/api/v1/drivers')
app.register_blueprint(order_api, url_prefix='/api/v1/orders')
app.register_blueprint(shipment_api, url_prefix='/api/v1/shipments')
migrate = Migrate(app, db)
CORS(app)

if __name__ == '__main__':
    # run app
    app.run(debug=True, host="0.0.0.0",port=5000)