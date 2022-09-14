from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.users_model import Users
from flask_app.models.recipes_model import Recipes
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/register', methods = ['POST'])
def register_info():
    if not Users.validate(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : hashed_pw
    }
    session['login_id'] = Users.register_user(data)
    return redirect('/recipes')

@app.route('/login', methods = ['POST'])
def login_info():
    data = {
        'email' : request.form['login_email']
    }
    user_from_db = Users.check_email(data)
    if not user_from_db:
        flash("Invalid credentials", "log")
        return redirect('/')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['login_password']):
        flash("Invalid credentials", "log")
        return redirect('/')
    session['login_id'] = user_from_db.id
    return redirect('/recipes')

@app.route('/logout')
def logout():
    del session['login_id']
    return redirect('/')

@app.route('/recipes')
def all_recipes():
    if not "login_id" in session:
        return redirect('/')
    recipes = Recipes.recipes_page()
    data = {
        'id' : session['login_id']
    }
    logged_user= Users.check_user(data)
    return render_template('welcome.html', recipes = recipes, logged_user = logged_user)