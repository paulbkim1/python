from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojos_model import Dojos


@app.route('/dojos')
def dojos():
    all_dojos = Dojos.get_all()
    return render_template('dojos.html', all_dojos = all_dojos)


@app.route('/dojos/<int:id>')
def show_ninjas(id):
    data = {
        'id' : id
    }
    show_dojo = Dojos.get_ninjas(data)
    return render_template('dojo_show.html', show_dojo = show_dojo)


@app.route('/dojos/create', methods = ['POST'])
def add_dojos():
    Dojos.create_dojos(request.form)
    return redirect('/dojos')




