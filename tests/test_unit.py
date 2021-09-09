from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Athletes, Results

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY = 'TEST_SECRET_KEY',
            WTF_CSRF_ENEBLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        athleteTest = Athletes(first_name ="John", last_name = "Smith", gender = "Male", age = 22 , country="UK")
        db.session.add(athleteTest)
        db.session.commit
        resultTest = Results(year = 2012, event = "Men's 100m", medal = "Gold", fk_athlete_ID = 1)
        db.session.add(resultTest)
        db.session.commit

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_athlete(self):
        response = self.client.get(url_for('athletes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)

    def test_result(self):
        response = self.client.get(url_for('results'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Gold", response.data)
    

class TestAddAthlete(TestBase):
    def test_add_athlete(self):
        response = self.client.post(
            url_for('add_athlete')

        )