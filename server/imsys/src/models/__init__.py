from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .client import Client
from .driver import Driver
from .truck import Truck
from .order import Order