from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self,data):
        self.name = data['name']
        self.email = data['email']
        self.rating = data['rating']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_survey(cls,data):
        query = "INSERT INTO dojos (name, email, rating, comment) VALUES (%(name)s, %(email)s, %(rating)s, %(comment)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def submitted_info(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC LIMIT 1;"
        return connectToMySQL(DATABASE).query_db(query)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 1:
            is_valid = False
            flash("Name must be provided")
        if len(data['email']) < 1:
            is_valid = False
            flash("Email must be provided")
        if 'rating' not in data:
            is_valid = False
            flash("Rating must be provided")
        if len(data['comment']) < 1:
            is_valid = False
            flash("Comment must be provided")
        return is_valid