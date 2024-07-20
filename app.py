from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api
from flask_login import LoginManager, login_required, login_user, current_user
from controller.guarderia_controller import GuarderiaController
from controller.perro_controller import PerroController
from models.usuario import Usuario
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import os

secret_key = os.urandom(24)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:Samuel0710@localhost/tablas'
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return usuario
    return None

@app.route("/")
def main():
    return "Felicidades, ingresaste al sistema"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario.query.filter_by(username=username, password=password).first()
        if usuario:
            login_user(usuario)
            if Usuario.is_admin:
                return redirect(url_for("perrocontroller"))
            else:
                return redirect(url_for("cuidadorcontroller"))
    return render_template("login.html")


api.add_resource(GuarderiaController, '/guarderias')
api.add_resource(PerroController, '/perros')
