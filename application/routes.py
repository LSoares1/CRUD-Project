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


@app.route('/add_athlete', methods=['GET', 'POST'])
def add_athlete():
    form = AddAthlete()
    if request.method == 'POST' and form.validate_on_submit():
        athlete_data = Athletes(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            gender = form.gender.data,
            date_of_birth = form.dob.data,
            country = form.country.data
            )
        db.session.add(athlete_data)
        db.session.commit()   
        return redirect(url_for('add_athlete'))
    
    return render_template('add_athlete.html',form=form)

@app.route('/add_result', methods=['GET', 'POST'])
def add_result():
    form = AddResult()
    if request.method == 'POST' and form.validate_on_submit():
        result_data = Results(
            date = form.date.data,
            event = form.event.data,
            medal = form.medal.data,
            )
        db.session.add(result_data)
        db.session.commit()
        return redirect(url_for('add_result'))

    return render_template('add_result.html',form=form)

@app.route('/athletes')
def athletes():
    athletesData = Athletes.query.all()
    return render_template('athletes.html', athletes=athletesData)

@app.route('/results')
def results():
    resultsData = results.query.all()
    return render_template('results.html', results=resultsData)
    