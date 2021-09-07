from application import app, db
from application.models import Athletes, Results
from application.forms import AddAthlete, AddResult
from flask import render_template, url_for, redirect, request

@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/addathlete', methods=['GET', 'POST'])
def add_athlete():
    form = AddAthlete()
    if form.validate_on_submit():
        athlete_data = Athletes(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            gender = form.gender.data,
            date_of_birth = form.dob.data,
            country = form.country.data
        )
        return 'Form successfully submitted'

    return render_template('addathlete.html',form=form)

@app.route('/addresult', methods=['GET', 'POST'])
def add_result():
    form = AddResult()
    result_data = Results(
        date = form.date.data,
        event = form.event.data,
        medal = form.medal.data,
        )
    db.session.add(result_data)
    db.session.commit

    return render_template('addresult.html',form=form)

@app.route('athletes')
def athletes():
    athletes = Athletes.query.all()
    