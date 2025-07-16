# models.py

from datetime import datetime
from config import db, ma

class DATA(db.Model):
    __tablename__ = "Datas"
    id = db.Column(db.Integer, primary_key=True)
    Parameters = db.Column(db.String(32), unique=True)
    value = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DATA
        load_instance = True
        sqla_session = db.session

Data_schema = PersonSchema()
Datas_schema = PersonSchema(many=True)