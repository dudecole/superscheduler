from superscheduler import db
from models import Contractor


db.create_all()
db.session.commit()
