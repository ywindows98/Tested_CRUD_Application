from datetime import datetime
import pytest

import sys
sys.path.append('..')

from backend.tests.test_base import BaseUserTestCase
from backend.src.models import User, Subscription, StatusEnum

@pytest.mark.run(order=5)
class TestUserDelete(BaseUserTestCase):
    def test_delete_users(self):
        """Test DELETE /user/id"""
        sample_users = []
        sample_users.append(self.sample_full_data)
        sample_users.append(self.sample_no_date)
        sample_users.append(self.sample_no_location)

        for sample in sample_users:
            self.client.post('/user', json=sample)

        for i in range(len(sample_users)):
            response = self.client.delete(f'/user/{i+1}')
            users = User.query.all()
            self.assertEqual(response.status_code, 204, 'Response status code for a good delete request is not 204')
            self.assertEqual(len(sample_users) - (i+1), len(users), 'Number of users in the database was not decreased by one after a delete request')

            with self.app.app_context():
                user = User.query.filter_by(username=sample_users[i]['username']).first()
                username = sample_users[i]['username']
                self.assertIsNone(user, f'There is still user with a {username} username in database after a delete request')  # Ensure the user no longer exists

    def test_delete_no_user(self):
        response = self.client.delete(f'/user/12')
        self.assertEqual(response.status_code, 404, 'Response status code is not 404 when there is no user with given id')
