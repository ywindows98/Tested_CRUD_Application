from datetime import datetime

import sys
sys.path.append('..')

from backend.tests.test_base import BaseUserTestCase
from backend.src.models import User, Subscription, StatusEnum

class TestUserCreate(BaseUserTestCase):
    def _check_response_for_successful_creation(self, sample_data):
        """Post user from sample_data and test received response"""
        response = self.client.post('/user', json=sample_data)

        # HTTP response
        self.assertEqual(response.status_code, 201, 'Response status code for a good request is not a 201 Created')

    def _select_user_by_username(self, username):
        # Select user from db
        with self.app.app_context():
            user = User.query.filter_by(username=username).first()
            self.assertIsNotNone(user, f'No user with {username} username in database')  # Ensure the user exists

        return user

    def _check_required_fields(self, sample_data, user):
        self.assertEqual(user.username, sample_data['username'], 'Created user has wrong username')
        self.assertEqual(user.email, sample_data['email'], 'Created user has wrong email')
        self.assertEqual(user.subscription_id, sample_data['subscription_id'], 'Created user has wrong subscription_id')

    def _check_response_for_unsuccessful_creation(self, sample_data):
        """Post user from sample_data and test received response"""
        response = self.client.post('/user', json=sample_data)

        # HTTP response
        self.assertEqual(response.status_code, 400, 'Response status code for a bad request is not a 400 Bad Request')

    def test_create_user_full_data(self):
        """Test POST /user for user with full data"""
        sample_data = self.sample_full_data
        self._check_response_for_successful_creation(sample_data)

        user = self._select_user_by_username(sample_data['username'])

        self._check_required_fields(sample_data, user)

        self.assertEqual(user.date_registered, sample_data['date_registered'], 'Created user has wrong date_registered')
        self.assertEqual(user.location, sample_data['location'], 'Created user has wrong location')
        self.assertEqual(user.status, StatusEnum[sample_data['status']], 'Created user has wrong status')

    def test_create_user_no_date(self):
        """Test POST /user for user with no registration date"""
        sample_data = self.sample_no_date
        self._check_response_for_successful_creation(sample_data)

        user = self._select_user_by_username(sample_data['username'])

        self._check_required_fields(sample_data, user)

        self.assertIsNotNone(user.date_registered, 'Created user has no default date_registered')
        self.assertEqual(user.location, sample_data['location'], 'Created user has wrong location')
        self.assertEqual(user.status, StatusEnum[sample_data['status']], 'Created user has wrong status')

    def test_create_user_no_location(self):
        """Test POST /user for user with no location"""
        sample_data = self.sample_no_location
        self._check_response_for_successful_creation(sample_data)

        user = self._select_user_by_username(sample_data['username'])

        self._check_required_fields(sample_data, user)

        self.assertEqual(user.date_registered, sample_data['date_registered'], 'Created user has wrong date_registered')
        self.assertIsNone(user.location, 'Created user with no given location has a location')
        self.assertEqual(user.status, StatusEnum[sample_data['status']], 'Created user has wrong status')

    def test_create_user_no_status(self):
        """Test POST /user for user with no status """
        sample_data = self.sample_no_status
        self._check_response_for_successful_creation(sample_data)

        user = self._select_user_by_username(sample_data['username'])

        self._check_required_fields(sample_data, user)

        self.assertEqual(user.date_registered, sample_data['date_registered'], 'Created user has wrong date_registered')
        self.assertEqual(user.location, sample_data['location'], 'Created user has wrong location')
        self.assertEqual(user.status, StatusEnum.OFFLINE, 'Created user has no default status or a wrong status')

    def test_create_user_no_data(self):
        """Test POST /user for user with no date"""
        sample_data = self.sample_no_data
        self._check_response_for_unsuccessful_creation(sample_data)

    def test_create_user_no_username(self):
        """Test POST /user for user with no username"""
        sample_data = self.sample_no_username
        self._check_response_for_unsuccessful_creation(sample_data)

    def test_create_user_no_email(self):
        """Test POST /user for user with no email"""
        sample_data = self.sample_no_email
        self._check_response_for_unsuccessful_creation(sample_data)

    def test_create_user_no_subscription_id(self):
        """Test POST /user for user with no subscription_id"""
        sample_data = self.sample_no_subscription_id
        self._check_response_for_unsuccessful_creation(sample_data)
