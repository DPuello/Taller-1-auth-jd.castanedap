from db import db


class Dog(db.Model):
    __tablename__ = "dogs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    breed = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    id_daycare = db.Column(
        db.Integer,
        db.ForeignKey("daycares.id"),
        nullable=False
    )
    id_caretaker = db.Column(
        db.Integer,
        db.ForeignKey("caretakers.id"),
        nullable=False
    )
