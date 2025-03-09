import datetime
import enum

from .database import db

class Subscription(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class StatusEnum(enum.Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.datetime.today(), nullable=False)
    location = db.Column(db.String(60), unique=False, nullable=True)
    status = db.Column(db.Enum(StatusEnum), default=StatusEnum.OFFLINE.name, nullable=False)

    subscription = db.relationship('Subscription', backref='users')

    def to_dict(self):
        """Convert the object to a dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'subscription_id': self.subscription_id,
            'date_registered': self.date_registered,
            'location': self.location,
            'status': self.status
        }
