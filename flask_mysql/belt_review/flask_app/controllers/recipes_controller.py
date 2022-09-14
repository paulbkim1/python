from crypt import methods
from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.users_model import Users
from flask_app.models.recipes_model import Recipes

@app.route('/recipes/new')
def new_recipe():
    if not "login_id" in session:
        return redirect('/')
    return render_template('add_recipe.html')

@app.route('/recipes/new/add', methods = ['POST'])
def create_recipe():
    if not Recipes.validate(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id' : session['login_id']
    }
    Recipes.add_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if not "login_id" in session:
        return redirect('/')
    recipes = Recipes.select_recipe({'id':id})
    return render_template('edit_recipe.html', recipes = recipes)

@app.route('/recipes/edit/<int:id>/info', methods = ['POST'])
def edit_recipe_info(id):
    if not Recipes.validate(request.form):
        return redirect(f"/recipes/edit/{id}")
    data = {
        **request.form,
        'id' : id
    }
    Recipes.edit_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    data = {
        'id' : id
    }
    Recipes.delete_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if not "login_id" in session:
        return redirect('/')
    data = {
        'id' : id
    }
    show_recipe = Recipes.display_recipe(data)
    return render_template('view_recipe.html', show_recipe = show_recipe)