from crypt import methods
from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.login_model import Login
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def login():
    if "login_id" in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    if not Login.validate(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : hashed_pw
    }
    session['login_id'] = Login.created_user(data)
    return redirect('/dashboard')

@app.route('/dashboard')
def success():
    if not "login_id" in session:
        return redirect('/')
    return render_template('success.html')

@app.route('/logout')
def logout():
    del session['login_id']
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login_user():
    data = {
        'email' : request.form['login_email']
    }
    user_from_db = Login.get_email(data)
    if not user_from_db:
        flash("Invalid credentials", "log")
        return redirect('/')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['login_password']):
        flash("Invalid credentials", "log")
        return redirect('/')
    session['login_id'] = user_from_db.id
    return redirect('/dashboard')