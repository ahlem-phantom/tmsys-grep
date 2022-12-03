import datetime
import enum
from . import db
from sqlalchemy.sql import func

class TruckStatus(enum.Enum):
    Available = "Available",
    Assigned = "Assigned"

class TruckType(enum.Enum):
    Van = "Van",
    Box = "Box Truck"
    Trailer = "Semi Trailer Truck"


class Truck(db.Model):
    __tablename__ = "truck"
    truck_id = db.Column(db.Integer, primary_key=True,autoincrement=True);
    truck_name = db.Column(db.String(255));
    truck_type = db.Column(db.Enum(TruckType), nullable=False);
    truck_plate = db.Column(db.String(255));
    truck_year = db.Column(db.String(255));
    truck_model = db.Column(db.String(255));
    truck_capacity = db.Column(db.Integer);
    truck_size = db.Column(db.Integer);
    truck_engine = db.Column(db.String(255));
    truck_color = db.Column(db.String(255));
    truck_status = db.Column(db.Enum(TruckStatus), nullable=False, server_default="Available");
    created_at = db.Column(db.Date, server_default=func.now());
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    shipment = db.relationship('Shipment', uselist=False, back_populates='truck')

    def __init__(self, truck_name,truck_type,truck_plate, truck_year, truck_model, truck_capacity, truck_size, truck_engine, truck_color):
        self.truck_name = truck_name
        self.truck_type = truck_type
        self.truck_plate = truck_plate
        self.truck_year = truck_year
        self.truck_model = truck_model
        self.truck_capacity = truck_capacity
        self.truck_size = truck_size
        self.truck_engine = truck_engine
        self.truck_color = truck_color
        #self.driver_id = driver_id

    def __repr__(self):
        return '%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s' % (self.truck_id, self.truck_name, self.truck_plate, self.truck_year, self.truck_model, self.truck_capacity, self.truck_size, self.truck_engine, self.truck_color , self.truck_status, self.created_at)
    

    