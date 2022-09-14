from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users_model
from flask import flash

class Users:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    