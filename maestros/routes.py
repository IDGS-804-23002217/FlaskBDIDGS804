from . import maestros

from flask import Flask, render_template, request, redirect, url_for
import forms
from models import Maestros


@maestros.route("/maestros", methods=['GET', 'POST'])
@maestros.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros)

@maestros.route('/perfil/<nombre>') #Como ahora son del modulo de maestros ahora se empieza por @maestros, no @route
def perfil(nombre):
    return f"Perfil de {nombre}"
