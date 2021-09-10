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
    def test_view_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_athlete(self):
        response = self.client.get(url_for('athletes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)
        
    def test_view_result(self):
        response = self.client.get(url_for('results'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Gold", response.data)

    def test_view_add_athlete(self):
        response = self.client.get(url_for('add_athlete'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add an Athlete', response.data)

    def test_view_add_result(self):
        response = self.client.get(url_for('add_result'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add a Result", response.data)

class TestAddAthletes(TestBase):
    def test_add_athlete(self):
        response = self.client.post(
            url_for('add_athlete'),
            data = dict(first_name="Test", last_name="Athlete", gender = "Male", age = 32, country = "UK"),
            follow_redirects=True
        )
        self.assertIn(b"Test", response.data)

class TestUpdateAthlete(TestBase):
    def test_update_athlete(self):
        response = self.client.post(
            url_for('update_athlete', aid = 1),
            data = dict(first_name ="James", last_name = "Brown", gender = "Male", age = 25, country =" UK"),
            follow_redirects=True
        )
        self.assertIn(b'James', response.data)
        self.assertEqual(response.status_code, 200)
        
        

class TestUpdateResult(TestBase):
    def test_update_result(self):
        response = self.client.post(
            url_for('update_result', rid = 1),
            data = dict(year = 2016, event = "Men's Long Jump", medal = "Silver", fk_athlete_ID = 1),
            follow_redirects=True
        )
        self.assertIn(b"Silver", response.data)
        self.assertEqual(response.status_code, 200)

class TestDeleteAthlete(TestBase):
    def test_delete_athlete(self):
        response = self.client.post(
            url_for("delete_athlete", aid=1),
            follow_redirects=True
            )
        self.assertNotIn(b"John", response.data)

class TestDeleteResult(TestBase):
    def test_delete_result(self):
        response = self.client.post(
            url_for("delete_result", rid=1),
            follow_redirects=True
            )
        self.assertNotIn(b'2012', response.data)
        
        
           