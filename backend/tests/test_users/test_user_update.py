from datetime import datetime
import pytest

import sys
sys.path.append('..')

from backend.tests.test_base import BaseUserTestCase
from backend.src.models import User, Subscription, StatusEnum


@pytest.mark.run(order=4)
class TestUserCreate(BaseUserTestCase):
    def _check_returned_user(self, sample_data, user_json):
        """
        Check given user_json data to be as expected from stored object.
        Also check if default values are correctly returned.
        """
        self.assertIn('username', user_json, 'Returned user has no username')
        self.assertIn('email', user_json, 'Returned user has no email')
        self.assertIn('subscription_id', user_json, 'Returned user has no subscription_id')
        self.assertIn('date_registered', user_json, 'Returned user has no date_registered')
        if 'location' in sample_data:
            self.assertIn('location', user_json, 'Returned user that has to have location have no location')
        self.assertIn('status', user_json, 'Returned user has no status')

        self.assertEqual(sample_data['username'], user_json['username'],
                         'Username of the returned user is wrong')
        self.assertEqual(sample_data['email'], user_json['email'],
                         'Email of the returned user is wrong')
        self.assertEqual(sample_data['subscription_id'], user_json['subscription_id'],
                         'Subscription_id of the returned user is wrong')

        if 'date_registered' in sample_data:
            self.assertEqual(sample_data['date_registered'],
                             datetime.strptime(user_json['date_registered'], "%a, %d %b %Y %H:%M:%S GMT"),
                             'Date_registered of the returned user is wrong')
        else:
            self.assertIsNotNone(user_json['date_registered'],
                                 'Returned user has no Date_registered')

        if 'location' in sample_data:
            self.assertEqual(sample_data['location'], user_json['location'],
                             'Location of the returned user is wrong')

        if 'status' in sample_data:
            self.assertEqual(sample_data['status'], user_json['status'],
                             'Status of the returned user is wrong')
        else:
            self.assertEqual(StatusEnum.OFFLINE.name, user_json['status'],
                             'Status of the returned user is wrong')

    def _select_user_by_username(self, username):
        """Select user by given username and check if user with such username exists"""
        # Select user from db
        with self.app.app_context():
            user = User.query.filter_by(username=username).first()
            self.assertIsNotNone(user, f'No user with {username} username in database')  # Ensure the user exists

        return user

    def _check_required_fields(self, sample_data, user):
        """Test if required values were correctly written to the database"""
        self.assertEqual(user.username, sample_data['username'], 'Updated user has wrong username')
        self.assertEqual(user.email, sample_data['email'], 'Updated user has wrong email')
        self.assertEqual(user.subscription_id, sample_data['subscription_id'], 'Updated user has wrong subscription_id')

    def test_update_user_full_data(self):
        """Test PUT /user/id with full data"""
        sample_full_data = self.sample_full_data
        sample_changed_data = self.sample_full_data_changed

        self.client.post('/user', json=sample_full_data)
        response = self.client.put('/user/1', json=sample_changed_data)

        self.assertEqual(response.status_code, 200, 'Response status code for a good request is not 200')

        user = self._select_user_by_username(sample_changed_data['username'])

        self._check_required_fields(sample_changed_data, user)

        self.assertEqual(user.date_registered, sample_changed_data['date_registered'], 'Updated user has wrong date_registered')
        self.assertEqual(user.location, sample_changed_data['location'], 'Updated user has wrong location')
        self.assertEqual(user.status, StatusEnum[sample_changed_data['status']], 'Updated user has wrong status')

    def test_update_user_data_addition(self):
        """Test PUT /user/id with added data"""
        sample_required_data = self.sample_required_data
        sample_changed_data = self.sample_added_full_data

        self.client.post('/user', json=sample_required_data)
        response = self.client.put('/user/1', json=sample_changed_data)

        self.assertEqual(response.status_code, 200, 'Response status code for a good request is not 200')

        user = self._select_user_by_username(sample_changed_data['username'])

        self._check_required_fields(sample_changed_data, user)

        self.assertEqual(user.date_registered, sample_changed_data['date_registered'], 'Updated user has wrong date_registered')
        self.assertEqual(user.location, sample_changed_data['location'], 'Updated user has wrong location')
        self.assertEqual(user.status, StatusEnum[sample_changed_data['status']], 'Updated user has wrong status')

    def test_update_user_data_reduction(self):
        """Test PUT /user/id with reduced data"""
        sample_full_data = self.sample_full_data
        sample_changed_data = self.sample_required_data

        self.client.post('/user', json=sample_full_data)
        response = self.client.put('/user/1', json=sample_changed_data)

        self.assertEqual(response.status_code, 200, 'Response status code for a good request is not 200')

        user = self._select_user_by_username(sample_changed_data['username'])

        self._check_required_fields(sample_changed_data, user)

        self.assertEqual(user.date_registered, sample_full_data['date_registered'], 'Updated user has wrong date_registered')
        self.assertIsNone(user.location, 'Updated user has location when it was updated to have no location')
        self.assertEqual(user.status, StatusEnum[sample_full_data['status']], 'Updated user has wrong status')

    def test_update_user_no_data(self):
        """Test PUT /user/id with no data"""
        sample_required_data = self.sample_required_data
        sample_changed_data = self.sample_no_data

        self.client.post('/user', json=sample_required_data)
        response = self.client.put('/user/1', json=sample_changed_data)

        self.assertEqual(response.status_code, 400, 'Response status code for a bad request is not a 400 Bad Request')

    def test_update_user_no_required_data(self):
        """Test PUT /user/id with no required data"""
        sample_required_data = self.sample_required_data
        self.client.post('/user', json=sample_required_data)

        sample_changed_data = self.sample_no_username
        response = self.client.put('/user/1', json=sample_changed_data)

        self.assertEqual(response.status_code, 400, 'Response status code for a bad request is not a 400 Bad Request')

        sample_changed_data = self.sample_no_email
        response = self.client.put('/user/1', json=sample_changed_data)

        self.assertEqual(response.status_code, 400, 'Response status code for a bad request is not a 400 Bad Request')

        sample_changed_data = self.sample_no_subscription_id
        response = self.client.put('/user/1', json=sample_changed_data)

        self.assertEqual(response.status_code, 400, 'Response status code for a bad request is not a 400 Bad Request')
