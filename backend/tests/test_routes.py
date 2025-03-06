import unittest
from backend import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True # enable testing mode for flask
        self.client = app.test_client()