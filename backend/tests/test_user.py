import unittest

import sys
sys.path.append('..')

from backend.app import app, db

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True # enable testing mode for flask
        self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

