import unittest
import pytest

import sys
sys.path.append('..')

from backend.app import app


@pytest.mark.run(order=1)
class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True # enable testing mode for flask
        self.client = app.test_client()

    def test_home(self):
        """Test the home / route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')  # Check response is JSON
        self.assertIn('message', response.json)  # Ensure 'message' key exists
        self.assertEqual(response.json['message'], 'Home page')  # Check message value
