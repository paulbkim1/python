from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

class Authors:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DATABASE).query_db(query)
        author_list = []
        for i in results:
            results_instance = cls(i)
            author_list.append(results_instance)
        return author_list

    @classmethod
    def create_author(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def add_authors_favorite(cls,data):
        query = 'INSERT INTO favorites (author_id, book_id) VALUES (%(id)s, %(favorite_books)s);'
        return connectToMySQL(DATABASE).query_db(query, data)
    