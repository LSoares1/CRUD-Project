from application import app, db
from application.models import Athletes, Results
from application.forms import AddAthlete, AddResult, UpdateAthlete, UpdateResult
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
            fk_athlete_ID = form.athlete.data
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
    resultsData = Results.query.all()
    return render_template('results.html', results=resultsData)
    
@app.route('/delete_athlete/<int:aid>')
def delete_athlete(aid):
    athlete_to_delete = Athletes.query.get(aid)
    db.session.delete(athlete_to_delete)
    db.session.commit()
    return redirect(url_for('athletes'))

@app.route('/delete_result/<int:rid>')
def delete_result(rid):
    result_to_delete = Results.query.get(rid)
    db.session.delete(result_to_delete)
    db.session.commit()
    return redirect(url_for('results'))

@app.route('/update_athlete/<int:aid>', methods=['GET','POST'])
def update_athlete(aid):
    form = UpdateAthlete()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        gender = form.gender.data
        date_of_birth = form.dob.data
        country = form.country.data
        athlete = Athletes.query.get(aid)
        athlete.first_name = first_name
        athlete.last_name = last_name
        athlete.gender = gender
        athlete.date_of_birth = date_of_birth
        athlete.country = country
        db.session.commit()
    
    return render_template('update_athlete.html',form=form)

@app.route('/update_result/<int:aid>', methods=['GET','POST'])
def update_result(aid):
    form = UpdateResuly()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        gender = form.gender.data
        date_of_birth = form.dob.data
        country = form.country.data
        result = Results.query.get(aid)
        result.first_name = first_name
        result.last_name = last_name
        result.gender = gender
        result.date_of_birth = date_of_birth
        result.country = country
        db.session.commit()
    
    return render_template('update_result.html',form=form)