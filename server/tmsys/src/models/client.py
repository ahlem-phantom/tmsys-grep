from . import db


class Client(db.Model):
    __tablename__ = "client"
    client_id = db.Column(db.Integer, primary_key=True);
    company_name = db.Column(db.String(255));
    company_address = db.Column(db.String(255));
    company_phone = db.Column(db.String(255));
    company_email = db.Column(db.String(255));
    orders = db.relationship('Order', backref='client');

    
    def __init__(self, company_name,company_address, company_phone, company_email):
        self.company_name =  company_name
        self.company_address = company_address
        self.company_phone = company_phone
        self.company_email = company_email


    def __repr__(self):
        return '%s/%s/%s/%s/%s' % ( self.company_name, self.company_address, self.company_phone, self.company_email)
    

