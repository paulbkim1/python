from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.survey_model import Survey

@app.route('/')
def form_page():
    return render_template('form.html')

@app.route('/form_data', methods= ['POST'])
def form_data():
    if not Survey.validate(request.form):
        return redirect('/')
    print(Survey.create_survey(request.form))
    return redirect('/result')

@app.route('/result')
def submitted_info():
    results = Survey.submitted_info()
    print(results)
    return render_template('results.html', results = results)