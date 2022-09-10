from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojos_model import Dojos
from flask_app.models.ninjas_model import Ninjas

@app.route('/ninjas')
def create_ninja():
    current_dojos = Dojos.get_all()
    return render_template('new_ninja.html', current_dojos = current_dojos)


@app.route('/ninjas/create', methods = ['POST'])
def new_ninja():
    Ninjas.new_ninjas(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')