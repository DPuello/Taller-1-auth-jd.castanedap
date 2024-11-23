from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from models.dog import Dog
from db import db
from flask_login import login_required, current_user

dog_blueprint = Blueprint('dogs', __name__, url_prefix='/dogs')


@dog_blueprint.route('/', methods=['GET'])
@login_required
def get_dogs():
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    dogs = Dog.query.all()
    return render_template('dogs.html', dogs=dogs)


@dog_blueprint.route('/', methods=['POST'])
@login_required
def create_dog():
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    data = request.get_json()
    new_dog = Dog(
        name=data['name'],
        breed=data['breed'],
        age=data['age'],
        weight=data['weight'],
        id_daycare=data['id_daycare'],
        id_caretaker=data['id_caretaker']
    )
    db.session.add(new_dog)
    db.session.commit()
    return jsonify({'message': 'Dog created successfully'}), 201


@dog_blueprint.route('/search/<string:name>', methods=['GET'])
@login_required
def get_dogs_by_name(name):
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    dogs = Dog.query.filter_by(name=name).all()
    return render_template('dog_by_name.html', name=name, amount=len(dogs))
