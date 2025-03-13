from flask import Flask
from flask_cors import CORS
from .database import db
import os

def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .models import User, Subscription, StatusEnum

    # Create tables
    with app.app_context():
        db.create_all()

    # Import Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app