import unittest

import os
import sys
sys.path.append('..')

from backend.src.database import db
from backend.src import create_app
from backend.src.models import User, Subscription, StatusEnum


class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test client and test database"""
        # cls.app = app
        cls.app = create_app(testing=True)
        cls.client = cls.app.test_client()


        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Drop all tables and clean up"""
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        """Start a new db session"""
        self.app = self.__class__.app
        self.client = self.__class__.client
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Roll back the changes"""
        db.session.rollback()
        self.app_context.pop()

    def test_create_user(self):
        """Test POST /user"""
        data = {
            'username': 'SampleUser1',
            'email': 'sampleemail@sample.com',
            'subscription_id': 2,
            'status': StatusEnum.ONLINE.name
        }
        response = self.client.post('/user', json=data)

        # HTTP response
        self.assertEqual(response.status_code, 201)
        self.assertIn('username', response.json)
        self.assertIn('subscription_id', response.json)
        self.assertEqual(response.json['username'], 'SampleUser1')
        self.assertEqual(response.json['subscription_id'], 2)

        # Verify DB
        with self.app.app_context():
            user = User.query.filter_by(username='SampleUser1').first()
            self.assertIsNotNone(user)  # Ensure the user exists
            self.assertEqual(user.email, 'sampleemail@sample.com')  # Ensure email matches


if __name__ == '__main__':
    unittest.main()