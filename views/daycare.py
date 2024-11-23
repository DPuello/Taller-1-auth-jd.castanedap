from flask import Blueprint, jsonify, render_template, redirect, url_for
from models.daycare import Daycare
from models.caretaker import Caretaker
from models.dog import Dog
from flask_login import login_required, current_user

daycare_blueprint = Blueprint(
    'daycares', __name__, url_prefix='/daycares')


@daycare_blueprint.route('/', methods=['GET'])
@login_required
def get_daycares():
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    daycares = Daycare.query.all()
    return render_template('daycares.html', daycares=daycares)


@daycare_blueprint.route('/favorita', methods=['GET'])
@login_required
def get_favorita():
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    daycare_with_caretakers = Daycare.query.filter_by(
        name='La favorita').first()
    if daycare_with_caretakers:
        caretakers = Caretaker.query.filter_by(
            id_daycare=daycare_with_caretakers.id).all()
        for caretaker in caretakers:
            caretaker.dogs = Dog.query.filter_by(
                id_caretaker=caretaker.id).all()
        return render_template(
            'la_favorita.html',
            caretakers=caretakers,
            daycare=daycare_with_caretakers
        )
    return jsonify({'message': 'Daycare not found'}), 404
