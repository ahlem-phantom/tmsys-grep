from sqlalchemy.sql import func
from . import db
import enum 

class OrderStatus(enum.Enum):
    CREATED = 'CREATED',
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
    order_address = db.Column(db.String(255));
    order_reference = db.Column(db.String(255));
    order_date = db.Column(db.Date);
    order_code = db.Column(db.String(255), nullable=False);
    order_ht = db.Column(db.String(255));
    order_tva = db.Column(db.String(255));
    order_ttc = db.Column(db.String(255));
    order_status = db.Column(db.Enum(OrderStatus), nullable=False,server_default="CREATED")
    date_received = db.Column(db.Date, server_default=func.now())


    def __init__(self, order_address, order_reference, order_date, order_code, order_ht, order_tva, order_ttc):
        self.order_address =  order_address
        self.order_reference =  order_reference
        self.order_date = order_date 
        self.order_code = order_code
        self.order_ht = order_ht
        self.order_tva = order_tva
        self.order_ttc = order_ttc 

    def __repr__(self):
        return '%s/%s/%s/%s/%s/%s/%s/%s/%s/%s' % (self.id, self.order_status,self.date_received, self.order_address, self.order_reference, self.order_date, self.order_code, self.order_ht, self.order_tva, self.order_ttc)
