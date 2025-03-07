from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from src.models import db, User, Subscription, StatusEnum
from src import populate

# load_dotenv("../backend_env.env")

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
def home():
    return jsonify({"message": "Home page"})

@app.route("/user", methods=["GET"])
def get_users():
    return jsonify({"message" : "Not implemented"}), 405

@app.route("/user", methods=["POST"])
def create_user():
    return jsonify({"message" : "Not implemented"}), 405

@app.route("/user/<int:id>", methods=["GET"])
def get_user():
    return jsonify({"message" : "Not implemented"}), 405

@app.route("/user/<int:id>", methods=["PUT"])
def update_user():
    return jsonify({"message" : "Not implemented"}), 405

@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user():
    return jsonify({"message" : "Not implemented"}), 405

if __name__ == "__main__":
    app.run()