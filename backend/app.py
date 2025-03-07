from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from models import db, User, Subscription, StatusEnum
import populate
from datetime import date
import time

load_dotenv("../backend_env.env")

# Initialize flaskapp
app = Flask(__name__)

# # Wait for postgres initialization
# time.sleep(5)

# DB URL from env
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app, because they are in separate files
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

populate.populate_subscriptions(app)

@app.route("/")
def hello():
    name = "Ferko"

    return "<h1 style='color:blue'>Hello There {}!</h1>".format(name)

@app.route("/users", methods=["GET","POST"])
def get_date():

    subscription = Subscription.query.filter_by(name="premium").first()
    if not subscription:
        raise ValueError("Invalid subscription type")

    new_user = User(username="sample", email="sample@gmail.com", subscription_id=subscription.id, status=StatusEnum.ONLINE)

    db.session.add(new_user)
    db.session.commit()

    return "<p>{}</p>"

if __name__ == "__main__":
    app.run()