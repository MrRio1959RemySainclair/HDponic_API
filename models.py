from datetime import datetime
from config import db, ma

class Datas(db.Model):
    __tablename__ = "Datas"
    id = db.Column(db.Integer, primary_key=True)
    Parameters = db.Column(db.String(32), unique=True)
    value = db.Column(db.Float)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class DatasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Datas
        load_instance = True
        sqla_session = db.session

Datas_schema = DatasSchema()
HDponic_schema = DatasSchema(many = True)