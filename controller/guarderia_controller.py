from flask import render_template, make_response
from flask_restful import Resource
from models.guarderia import Guarderia
from db import db

class GuarderiaController(Resource):
    def get(self):
        guarderias = Guarderia.query.all()
        return make_response(render_template("home.html", guarderias=guarderias))
    
    def post(self):
        guarderia = Guarderia(nombre="Mis pequeñas mascotas", direccion="Calle la esperanza", telefono="320585478")
        db.session.add(guarderia)
        db.session.commit()
        return "Guardería ok"