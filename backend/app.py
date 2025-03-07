from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
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

# Initialize db
db = SQLAlchemy(app)

# A user model
class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


# Create tables
with app.app_context():
    db.create_all()

@app.route("/")
def hello():
    name = "Ferko"

    return "<h1 style='color:blue'>Hello There {}!</h1>".format(name)

@app.route("/users", methods=["GET","POST"])
def get_date():
    new_user = AppUser(username="sample", email="sample@gmail.com")

    db.session.add(new_user)
    db.session.commit()

    return "<p>{}</p>"

if __name__ == "__main__":
    app.run()