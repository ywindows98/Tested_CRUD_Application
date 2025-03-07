import unittest

import sys
sys.path.append('..')

from backend.app import app, db
# from app import app
class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True # enable testing mode for flask
        self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home(self):
        """Test the home / route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')  # Check response is JSON
        self.assertIn("message", response.json)  # Ensure "message" key exists
        self.assertEqual(response.json["message"], "Home page")  # Check message value
