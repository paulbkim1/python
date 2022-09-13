from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.books_model import Books
from flask_app.models.authors_model import Authors

@app.route('/books')
def books_page():
    all_books = Books.get_books()
    return render_template('books.html', all_books = all_books)

@app.route('/books/create', methods = ['POST'])
def new_book():
    Books.add_book(request.form)
    return redirect('/authors')