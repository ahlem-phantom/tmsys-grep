from . import db
import enum 

class UserRole(enum.Enum):
    Client = 'Client',
    Manager = 'Manager',
    Admin = 'Admin',
    Driver = 'Driver'

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    token = db.Column(db.String(50), unique = True)
    role = db.Column(db.Enum(UserRole), nullable=False)
    
    def __init__(self, username, password, role, token):
        self.username = username
        self.password = password
        self.role = role
        self.token = token
    
    def __repr__(self):
        return '%s/%s/%s/%s/%s' % (self.id, self.username, self.password, self.role, self.token)
    