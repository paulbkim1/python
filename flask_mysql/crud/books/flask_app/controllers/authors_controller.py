from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.authors_model import Authors
from flask_app.models.books_model import Books

@app.route('/authors')
def author_list():
    authors = Authors.all_authors()
    return render_template('/authors.html', authors = authors)

@app.route('/authors/create', methods = ["POST"])
def new_author():
    Authors.create_author(request.form)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def author_show(id):
    all_books = Books.get_books()
    get_author = Authors.all_authors()
    return render_template('author_show.html', all_books = all_books)

@app.route('/author/favorite/<int:id>', methods = ['POST'])
def add_author_favorite(id):
    id = {
        'id' : id
    }
    Authors.add_authors_favorite(id, request.form)
    return redirect(f'/authors/{request.form["author_id"]}')
