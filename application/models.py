from application import db

class Athletes(db.Model):
    athlete_ID = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    results = db.relationship('Results', backref='athletes')

class Results(db.Model):
    result_ID = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable=False)
    medal  = db.Column(db.String(50), nullable=False)
    event = db.Column(db.String(100), nullable=False)
    fk_athlete_ID  = db.Column(db.Integer, db.ForeignKey('athletes.athlete_ID'))
    