from flask import Blueprint, jsonify, render_template, redirect, url_for
from models.caretaker import Caretaker
from models.dog import Dog
from db import db
from flask_login import login_required, current_user

caretaker_blueprint = Blueprint(
    'caretakers', __name__, url_prefix='/caretakers')


@caretaker_blueprint.route('/', methods=['GET'])
@login_required
def get_caretakers():
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    caretakers = Caretaker.query.all()
    return render_template('caretakers.html', caretakers=caretakers)


@caretaker_blueprint.route('/mario', methods=['GET'])
@login_required
def get_mario_dogs():
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    mario = Caretaker.query.filter_by(name="Mario").first()
    if not mario:
        return jsonify({"error": "Mario not found"}), 404

    # Get all dogs with weight <= 3 that aren't assigned to Mario yet
    available_dogs = Dog.query.filter(
        Dog.weight <= 3,
        Dog.id_caretaker != mario.id
    ).all()

    new_dogs = []
    # Assign these dogs to Mario
    for dog in available_dogs:
        dog.id_caretaker = mario.id
        new_dogs.append(dog)
    db.session.commit()

    # Get all Mario's dogs for display
    return render_template('dogs_of_mario.html', dogs=new_dogs)
