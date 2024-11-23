from db import db


class Caretaker(db.Model):
    __tablename__ = "caretakers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    id_daycare = db.Column(db.ForeignKey("daycares.id"), nullable=False)
    dogs = db.relationship('Dog', backref='caretaker', lazy=True)
