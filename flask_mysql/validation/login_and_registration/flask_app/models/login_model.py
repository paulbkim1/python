from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile('([A-Z][a-z]*)([\\s\\\'-][A-Z][a-z]*)*')


class Login:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def created_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters!", 'first_name')
        elif not NAME_REGEX.match(data['first_name']): 
            flash("First name can only contain letters!", 'first_name_characters')
            is_valid = False
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters!", 'last_name')
        elif not NAME_REGEX.match(data['last_name']): 
            flash("Last name can only contain letters!", 'last_name_characters')
            is_valid = False
        if len(data['email']) < 1:
            is_valid = False
            flash("email is not valid!", 'email')
        elif not EMAIL_REGEX.match(data['email']): 
            flash("email is not valid!", 'email')
            is_valid = False
        else:
            email_data = {
                'email' : data['email']
            }
            potential_user = Login.get_email(email_data)
            if potential_user:
                is_valid = False
                flash("Email already taken", "email_taken")
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters!", 'password')
        if data['confirm_password'] != data['password']:
            is_valid = False
            flash("Passwords do not match!", 'confirm_password')
        return is_valid
