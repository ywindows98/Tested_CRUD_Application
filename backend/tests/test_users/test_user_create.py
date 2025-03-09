from datetime import datetime

import sys
sys.path.append('..')

from backend.tests.test_base import BaseUserTestCase
from backend.src.models import User, Subscription, StatusEnum

class TestUserCreate(BaseUserTestCase):

    def test_create_user_full_data(self):
        """Test POST /user for user with full data"""
        sample_data = self.sample_full_data
        response = self.client.post('/user', json=sample_data)

        # HTTP response
        self.assertEqual(response.status_code, 201)
        self.assertIn('username', response.json)
        self.assertIn('subscription_id', response.json)
        self.assertEqual(response.json['username'], sample_data['username'])
        self.assertEqual(response.json['subscription_id'], sample_data['subscription_id'])

        # Verify DB user
        with self.app.app_context():
            user = User.query.filter_by(username=sample_data['username']).first()
            self.assertIsNotNone(user)  # Ensure the user exists
            self.assertEqual(user.email, sample_data['email'])
            self.assertEqual(user.subscription_id, sample_data['subscription_id'])
            self.assertEqual(user.date_registered, sample_data['date_registered'])
            self.assertEqual(user.location, sample_data['location'])
            self.assertEqual(user.status, StatusEnum[sample_data['status']])

    def test_create_user_no_date(self):
        """Test POST /user for user with no registration date"""
        sample_data = self.sample_no_date
        response = self.client.post('/user', json=sample_data)

        # HTTP response
        self.assertEqual(response.status_code, 201)

        # Verify DB user
        with self.app.app_context():
            user = User.query.filter_by(username=sample_data['username']).first()
            self.assertIsNotNone(user)  # Ensure the user exists
            self.assertEqual(user.email, sample_data['email'])
            self.assertEqual(user.subscription_id, sample_data['subscription_id'])
            self.assertIsNotNone(user.date_registered)
            self.assertEqual(user.location, sample_data['location'])
            self.assertEqual(user.status, StatusEnum[sample_data['status']])
