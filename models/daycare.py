from db import db


class Daycare(db.Model):
    __tablename__ = "daycares"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    dogs = db.relationship('Dog', backref='daycare', lazy=True)
