from . import db
import enum 
class DriverStatus(enum.Enum):
    assigned = 'Assigned',
    not_assigned = 'Not Assigned',


class Driver(db.Model):
    __tablename__ = "driver"
    id = db.Column(db.Integer, unique=True,primary_key=True,autoincrement=True) 
    driver_firstname= db.Column(db.String(255))
    driver_lastname = db.Column(db.String(255))
    driver_phone = db.Column(db.String(50), unique = True)
    driver_status = db.Column(db.Enum(DriverStatus), nullable=False, server_default="not_assigned")
    driver_email = db.Column(db.String(50), unique = True)
    driver_lat = db.Column(db.Float, primary_key=True)
    driver_lng = db.Column(db.Float, primary_key=True)
    driver_licence = db.Column(db.String(50), unique = True)
    trucks = db.relationship('Truck', backref='driver')

    def __init__(self, driver_firstname, driver_lastname, driver_phone, driver_email, driver_lat, driver_lng, driver_licence):
        self.driver_firstname = driver_firstname
        self.driver_lastname = driver_lastname
        self.driver_phone = driver_phone
        self.driver_email = driver_email
        self.driver_lat = driver_lat
        self.driver_lng = driver_lng
        self.driver_licence = driver_licence


    def __repr__(self):
        return '%s/%s/%s/%s/%s/%s/%s/%s/%s' % (self.id, self.driver_firstname, self.driver_lastname, self.driver_phone, self.driver_status, self.driver_email, self.driver_lat, self.driver_lng, self.driver_licence)
    