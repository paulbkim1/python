from crypt import methods
from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.email_model import Email


@app.route('/')
def email():
    return render_template('index.html')

@app.route('/create_email', methods = ["POST"])
def add_email():
    if not Email.validate(request.form):
        return redirect('/')
    Email.add_email(request.form)
    return redirect('/success')

@app.route('/success')
def list_emails():
    email_list = Email.list_emails()
    return render_template('success.html', email_list = email_list)

@app.route('/delete/<int:id>')
def delete_email(id):
    Email.delete({'id' : id})
    return redirect('/success')