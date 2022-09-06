from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'my_secret'

@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('counter.html')


@app.route('/process_1clicks', methods=['POST'])
def count_visits():
    print(request.form)
    return redirect('/')


@app.route('/process_2clicks', methods=['POST'])
def count_visits2():
    print(request.form)
    session['counter'] += 1
    return redirect('/')


@app.route('/destroy_session', methods=['POST'])
def clear():
    print(request.form)
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)