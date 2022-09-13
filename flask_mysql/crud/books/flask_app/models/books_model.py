from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

class Books:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_books = []
        for i in results:
            results_instance = cls(i)
            all_books.append(results_instance)
        return all_books

    @classmethod
    def add_book(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(pages)s);"
        return connectToMySQL(DATABASE).query_db(query, data)