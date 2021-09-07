from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, ValidationError

from application.models import Athletes,Results

class AddAthlete():
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    gender = SelectField("Gender", choices=[
        ("male","Male"),
        ("female","Female")
    ])
    dob = DateField("Date of Birth")
    country = StringField("Country")

class AddResult():
    date = DateField("Date")
    event = StringField("Event")
    medal = SelectField("Medal", choices=[
        ("gold","Gold"),
        ("silver","Silver"),
        ("bronze","Bronze"),
        ("none","None")
    ])

    