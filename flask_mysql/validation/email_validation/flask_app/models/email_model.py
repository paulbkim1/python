from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updatd_at = data['updatd_at']

    @classmethod
    def add_email(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def list_emails(cls):
        query = "SElECT * FROM emails ORDER BY id DESC;"
        return connectToMySQL(DATABASE).query_db(query)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['email']) < 1:
            is_valid = False
            flash("email is not valid!", 'email')
        elif not EMAIL_REGEX.match(data['email']): 
            flash("email is not valid!", 'email')
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)