from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rootroot@project-database.cnucpvtmhpb3.eu-west-1.rds.amazonaws.com:3306/project_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)

from application import routes