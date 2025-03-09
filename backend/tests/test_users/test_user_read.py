from datetime import datetime
import pytest

import sys
sys.path.append('..')

from backend.tests.test_base import BaseUserTestCase
from backend.src.models import User, Subscription, StatusEnum


@pytest.mark.run(order=3)
class TestUserRead(BaseUserTestCase):

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
                             'Location if the returned user is wrong')

        if 'status' in sample_data:
            self.assertEqual(sample_data['status'], user_json['status'],
                             'Status of the returned user is wrong')
        else:
            self.assertEqual(StatusEnum.OFFLINE.name, user_json['status'],
                             'Status of the returned user is wrong')
    def test_read_users(self):
        """Test GET /user to get list of users"""
        self.client.post('/user', json=self.sample_full_data)
        self.client.post('/user', json=self.sample_no_date)
        self.client.post('/user', json=self.sample_no_location)
        self.client.post('/user', json=self.sample_no_status)

        response = self.client.get('/user')

        self.assertEqual(response.status_code, 200, 'Response status code is not 200')
        self.assertIsInstance(response.json, list, 'Response is not a list of users')
        self.assertEqual(len(response.json), 4, 'Number of returned users in a list is not the same as a number of created users')

        self._check_returned_user(self.sample_full_data, response.json[0])
        self._check_returned_user(self.sample_no_date, response.json[1])
        self._check_returned_user(self.sample_no_location, response.json[2])
        self._check_returned_user(self.sample_no_status, response.json[3])

    def test_read_no_users(self):
        """Test GET /user to return a 404 uf there are no users in the db"""

        response = self.client.get('/user')

        self.assertEqual(response.status_code, 404, 'Response status code is not 404 when there are no users')

