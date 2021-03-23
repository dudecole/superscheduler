from superscheduler import db
from datetime import datetime


class Contractor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<ID %r>" % self.id
        