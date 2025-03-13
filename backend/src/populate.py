from .database import db
from .models import Subscription, User, StatusEnum
import requests


def populate_subscriptions(app):
    # Insert default subscription types if they don't exist
    default_subscriptions = ['standard', 'premium', 'premium+']

    with app.app_context():
        for sub in default_subscriptions:
            existing = Subscription.query.filter_by(name=sub).first()
            if not existing:
                db.session.add(Subscription(name=sub))

        db.session.commit()

def populate_users(app):
    """Populate db with sample users fow a showcase"""
    user1 = {
        'username': 'PopulatedUser1',
        'email': 'populated1@sample.com',
        'subscription_id': 1,
        'location': 'Kosice',
        'status': StatusEnum.ONLINE.name
    }

    user2 = {
        'username': 'PopulatedUser2',
        'email': 'populated2@sample.com',
        'subscription_id': 2,
        'location': 'Bratislava',
        'status': StatusEnum.OFFLINE.name
    }

    user3 = {
        'username': 'PopulatedUser3',
        'email': 'populated3@sample.com',
        'subscription_id': 3,
        'location': 'Presov',
        'status': StatusEnum.ONLINE.name
    }

    users = [user1, user2, user3]

    with app.app_context():
        for user in users:
            existing = User.query.filter_by(username=user['username']).first()
            if not existing:
                new_user = User(username=user['username'], email=user['email'], subscription_id=user['subscription_id'],
                                location=user['location'], status=user['status'])
                db.session.add(new_user)

        db.session.commit()
