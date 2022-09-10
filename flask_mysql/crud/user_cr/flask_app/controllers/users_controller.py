from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.users_model import Users

@app.route('/users')
def read():
    all_users = Users.get_all()
    return render_template('read.html', all_users = all_users)

@app.route('/users/<int:id>')
def one_user(id):
    one_user = Users.get_one({'id':id})
    return render_template('single_user.html', one_user = one_user)

@app.route('/users/new')
def create():
    return render_template('create.html')

@app.route('/users/create', methods = ['POST'])
def create_user():
    Users.create(request.form)
    return redirect ('/users')

@app.route('/users/<int:id>/edit')
def edit_users_form(id):
    data = {
        'id' : id
    }
    this_user = Users.get_one(data)
    return render_template("edit.html", this_user = this_user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_users(id):
    data = {
        **request.form,
        'id' : id
    }
    Users.update(data)
    return redirect('/users')

@app.route('/users/<int:id>/destroy')
def delete_user(id):
    data = {
        'id' : id
    }
    Users.delete(data)
    return redirect('/users')

