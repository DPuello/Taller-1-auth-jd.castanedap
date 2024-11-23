from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models.user import User

app_blueprint = Blueprint(
    'app', __name__, url_prefix='/')


@app_blueprint.route('/', methods=['GET'])
@login_required
def index():
    if not current_user.is_admin:
        return redirect(url_for('app.welcome'))
    return render_template('index.html')


@app_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for("app.index"))
        else:
            return "Invalid credentials"
    return render_template('login.html')


@app_blueprint.route("/welcome")
@login_required
def welcome():
    return render_template('welcome.html')


@app_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.login'))
