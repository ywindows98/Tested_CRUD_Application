import unittest

import sys
sys.path.append('..')

from backend.app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True # enable testing mode for flask
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
