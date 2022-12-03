from sqlalchemy.sql import func
from . import db
import enum 

class OrderStatus(enum.Enum):
    CREATED = 'CREATED',
    ASSIGNED = 'ASSIGNED',
    SHIPPING = "SHIPPING",
    DELIVERD = "DELIVERD",
    CANCELED = "CANCELED"

class OrderItems(enum.Enum):
    "CARTON",
    "CUBE",
    "BOX"

class Order(db.Model):
    __tablename__ = "order"
    order_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'))
    order_address = db.Column(db.String(255));
    order_reference = db.Column(db.String(255));
    order_date = db.Column(db.DateTime(timezone=False));
    order_code = db.Column(db.String(255), nullable=False);
    order_ht = db.Column(db.String(255));
    order_tva = db.Column(db.String(255));
    order_ttc = db.Column(db.String(255));
    order_status = db.Column(db.Enum(OrderStatus), nullable=False,server_default="CREATED")
    order_lat = db.Column(db.Float)
    order_lng = db.Column(db.Float)
    order_time_window = db.Column(db.Float)
    date_received = db.Column(db.DateTime(timezone=False), server_default=func.now());
    shipment = db.relationship('Shipment', backref='order');


    def __init__(self, client_id, order_address, order_reference, order_date, order_code, order_ht, order_tva, order_ttc, order_lng, order_lat):
        self.client_id = client_id
        self.order_address =  order_address
        self.order_reference =  order_reference
        self.order_date = order_date 
        self.order_code = order_code
        self.order_ht = order_ht
        self.order_tva = order_tva
        self.order_ttc = order_ttc 
        self.order_lng = order_lng
        self.order_lat = order_lat
        
    def __repr__(self):
        return '%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s' % (self.order_id, self.client_id,self.order_status,self.date_received, self.order_address, self.order_reference, self.order_date, self.order_code, self.order_ht, self.order_tva, self.order_ttc, self.order_lng , self.order_lat, self.order_time_window)
