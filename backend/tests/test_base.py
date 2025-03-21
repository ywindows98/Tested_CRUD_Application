import datetime
import unittest

import os
import sys
sys.path.append('..')

from backend.src.database import db
from backend.src import create_app
from backend.src.models import User, Subscription, StatusEnum


class BaseUserTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test client and test database"""
        cls.app = create_app(testing=True)
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            db.create_all()

        # Create sample users

        cls.sample_no_data = {

        }

        cls.sample_full_data = {
            'username': 'SampleFullData',
            'email': 'sampleemail1@sample.com',
            'subscription_id': 2,
            'date_registered': datetime.datetime(2025, 3, 1),
            'location': 'Kosice',
            'status': StatusEnum.ONLINE.name
        }

        cls.sample_no_date = {
            'username': 'UserNoDate',
            'email': 'sampleemail2@sample.com',
            'subscription_id': 1,
            'location': 'Kosice',
            'status': StatusEnum.ONLINE.name
        }

        cls.sample_no_location = {
            'username': 'UserNoLocation',
            'email': 'sampleemail3@sample.com',
            'subscription_id': 1,
            'date_registered': datetime.datetime(2025, 3, 1),
            'status': StatusEnum.ONLINE.name
        }

        cls.sample_no_status = {
            'username': 'UserNoStatus',
            'email': 'sampleemail4@sample.com',
            'subscription_id': 1,
            'date_registered': datetime.datetime(2025, 3, 1),
            'location': 'Kosice'
        }

        cls.sample_no_username = {
            'email': 'sampleemail5@sample.com',
            'subscription_id': 3
        }

        cls.sample_no_email = {
            'username': 'UserNoEmail',
            'subscription_id': 2
        }

        cls.sample_no_subscription_id = {
            'username': 'UserNoSubscription',
            'email': 'sampleemail7@sample.com',
        }

        # Samples for update method testing
        cls.sample_full_data_changed = {
            'username': 'SampleFullDataChanged',
            'email': 'sampleemailnew1@sample.com',
            'subscription_id': 1,
            'date_registered': datetime.datetime(2024, 3, 1),
            'location': 'Presov',
            'status': StatusEnum.OFFLINE.name
        }

        cls.sample_required_data = {
            'username': 'SampleRequiredData',
            'email': 'sampleemail12@sample.com',
            'subscription_id': 2,
        }

        cls.sample_added_full_data = {
            'username': 'SampleRequiredData',
            'email': 'sampleemail12@sample.com',
            'subscription_id': 2,
            'date_registered': datetime.datetime(2025, 2, 12),
            'location': 'Bratislava',
            'status': StatusEnum.ONLINE.name
        }


    @classmethod
    def tearDownClass(cls):
        """Drop all tables and clean up"""
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        """Start a new db session"""
        # self.app = self.__class__.app
        # self.client = self.__class__.client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """Roll back the changes"""
        db.session.rollback()
        self.app_context.pop()
