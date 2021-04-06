from superscheduler import db
from datetime import datetime


class Contractor(db.Model):
    # __tablename__ = 'contractors'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return "<ID %r>" % id
        