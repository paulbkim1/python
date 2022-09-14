from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users_model
from flask import flash

class Recipes:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_cooked = data['date_cooked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def recipes_page(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_recipes = []
            for i in results:
                this_recipe = cls(i)
                user_data = {
                    **i,
                    'id' : i['users.id'],
                    'created_at' : i['users.created_at'],
                    'updated_at' : i['users.updated_at']
                }
                this_user = users_model.Users(user_data)
                this_recipe.planner = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return []

    @classmethod
    def add_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, instruction, under, date_cooked, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(under)s, %(date_cooked)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters!", "name")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters!", "description")
            is_valid = False
        if len(data['instruction']) < 3:
            flash("Instructions must be at least 3 characters!", "instruction")
            is_valid = False
        if len(data['date_cooked']) < 1:
            flash("Invalid date!", "date_cooked")
            is_valid = False
        if "under" not in data:
            flash("Please choose if cook time was under 30 minutes!", "under")
            is_valid = False
        return is_valid

    @classmethod
    def edit_recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_cooked = %(date_cooked)s, under = %(under)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def check_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def select_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def display_recipe(cls,data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        this_recipe = cls(row)
        user_data = {
            **row,
            'id' : row['users.id'],
            'created_at' : row['users.created_at'],
            'updated_at' : row['users.updated_at']
        }
        planner = users_model.Users(user_data)
        this_recipe.planner = planner
        return this_recipe