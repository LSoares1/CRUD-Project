from application import app, db
from application.models import Athletes,Results
from flask import render_template

@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/athletes')

@app.route('/athletes/add')

