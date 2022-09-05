from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def form_page():
    return render_template('form.html')

@app.route('/form_data', methods= ['POST'])
def form_data():
    print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['rating'] = request.form['rating']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def results():
    name = session['name']
    email = session['email']
    rating = session['rating']
    comments = session['comments']
    return render_template('result.html', name = name, email = email, rating = rating, comments = comments)


if __name__=="__main__":
    app.run(debug=True)