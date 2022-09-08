from flask import Flask, render_template, request, redirect, session
from users_model import Users
app = Flask(__name__)

@app.route('/users')
def read():
    all_users = Users.get_all()
    return render_template('read.html', all_users = all_users)


@app.route('/users/new')
def create():
    return render_template('create.html')

@app.route('/users/create', methods = ['POST'])
def create_user():
    Users.create(request.form)
    return redirect ('/users')



if __name__ == "__main__":
    app.run(debug=True)