from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user
import os
from db import db, init_db
from models.user import User
from views.dog_view import dog_blueprint
from views.caretaker_view import caretaker_blueprint
from views.daycare import daycare_blueprint
from views.app_view import app_blueprint

file_path = os.path.join(os.path.abspath(os.getcwd()), "database", "site.db")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager = LoginManager(app)
login_manager.login_view = 'app.login'

db.init_app(app)
app.register_blueprint(app_blueprint)
app.register_blueprint(dog_blueprint)
app.register_blueprint(caretaker_blueprint)
app.register_blueprint(daycare_blueprint)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





with app.app_context():
    db.create_all()
    init_db(app)

if __name__ == "__main__":
    app.run(debug=True)
