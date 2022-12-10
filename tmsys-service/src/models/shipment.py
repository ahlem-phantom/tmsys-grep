from datetime import datetime
import enum
from . import db
from sqlalchemy.sql import func
from sqlalchemy import DDL, event

class ShipmentStatus(enum.Enum):
    WAITING = "WAITING",
    READY_TO_SHIP = "READY_TO_SHIP",
    ON_ROUTE = "ON_ROUTE",
    LOADING = "LOADING",
    UNLOADING = "UNLOADING",
    LATE = "LATE",
    STOPPED =  "STOPPED",
    NO_CONNECTION = "NO_CONNECTION"
    def __str__(self):
        return '%s' % self.value

"""
    IN_TRANSIT = "IN TRANSIT",
    DELIVERED = "DELIVERED",
    READY_TO_SHIP = "READY TO SHIP",
    DRAFT = "DRAFT",
    idle_timeout =  "idle timeout",
    no_connection = "no connection"
"""
class Shipment(db.Model):
    __tablename__ = "shipment"
    shipment_id = db.Column(db.Integer, unique=True,primary_key=True,autoincrement=True);
    time_created = db.Column(db.DateTime(timezone=False), server_default=func.now());
    time_updated = db.Column(db.DateTime(timezone=True), server_onupdate=func.now())
    shipment_seq = db.Column(db.String(255));
    shipment_status = db.Column(db.Enum(ShipmentStatus), nullable=False, server_default="WAITING");
    #OneToMany
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    #OneToOne
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.truck_id'))
    truck = db.relationship("Truck", back_populates="shipment")
    shipment_lat = db.Column(db.Float)
    shipment_lng = db.Column(db.Float)
    shipment_time = db.Column(db.Float)
    total_distance = db.Column(db.Float)
    total_time = db.Column(db.Float)

    def __init__(self, order_id, truck_id, shipment_seq, shipment_time):
        self.order_id = order_id
        self.truck_id = truck_id
        self.shipment_seq = shipment_seq
        self.shipment_time = shipment_time


    def __repr__(self):
        return '%s/%s/%s/%s/%s' % (self.shipment_id, self.shipment_status, self.order_id , self.truck_id, self.shipment_seq)
    

