from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired 
from application.models import Athletes,Results

class AddAthlete(FlaskForm):
    first_name = StringField("First Name", validators = [DataRequired()])
    last_name = StringField("Last Name", validators = [DataRequired()])
    gender = SelectField("Gender", choices=[
        ("male","Male"),
        ("female","Female")
    ], validators = [DataRequired()])
    age = IntegerField("Age", validators = [DataRequired()])
    country = StringField("Country", validators = [DataRequired()])
    submit = SubmitField("Add Athlete")

class AddResult(FlaskForm):
    
    year = IntegerField("Year", validators = [DataRequired()])
    event = StringField("Event", validators = [DataRequired()])
    medal = SelectField("Medal", choices=[
        ("gold","Gold"),
        ("silver","Silver"),
        ("bronze","Bronze"),
        ("none","None")
    ], validators = [DataRequired()])
    athleteList = SelectField("Athlete",choices=[], validators = [DataRequired()])

    submit = SubmitField("Add Result")

class UpdateAthlete(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    gender = SelectField("Gender", choices=[
        ("male","Male"),
        ("female","Female")
    ])
    dob = DateField("Date of Birth", format='%Y-%m-%d')
    country = StringField("Country")
    submit = SubmitField("Update Athlete")

class UpdateResult(FlaskForm):
    date = DateField("Date", format='%Y-%m-%d', validators = [DataRequired()])
    event = StringField("Event", validators = [DataRequired()])
    medal = SelectField("Medal", choices=[
        ("gold","Gold"),
        ("silver","Silver"),
        ("bronze","Bronze"),
        ("none","None")
    ], validators = [DataRequired()])
    
        
    submit = SubmitField("Update Result")    