from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'my_secret'

@app.route('/')
def counter():
    return render_template('counter.html')

@app.route('/process_clicks', methods=['POST'])
def count_visits():
    print(request.form)
    session['clicks'] = request.form['clicks']
    return redirect('/new_count')


@app.route('/new_count')
def new_count():
    clicks = session['clicks']
    return render_template('counter.html', clicks = clicks)




if __name__=="__main__":
    app.run(debug=True)