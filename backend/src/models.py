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
    date_registered = db.Column(db.DateTime, default=datetime.date.today(), nullable=False)
    location = db.Column(db.String(60), unique=False, nullable=True)
    status = db.Column(db.Enum(StatusEnum), default=StatusEnum.OFFLINE, nullable=False)

    subscription = db.relationship('Subscription', backref='users')

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}
