from application import app, db
from application.models import Athletes, Results
from flask import render_template, url_for, redirect, request

@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/home')
def home():
    return render_template('home.html')


