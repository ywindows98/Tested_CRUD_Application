from flask import Blueprint, jsonify, request
from .models import User
from .database import db
from datetime import datetime

main_bp = Blueprint('main', __name__)  # Create a blueprint

@main_bp.route('/')
def home():
    return jsonify({'message': 'Home page'})

@main_bp.route('/user', methods=['GET'])
def get_users():
    return jsonify({'message': 'Not implemented'}), 405

@main_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request data'}), 400

    # Retrieve model attributes from json
    username = data.get('username')
    email = data.get('email')
    subscription_id = data.get('subscription_id')
    date_registered = data.get('date_registered')
    location = data.get('location')
    status = data.get('status')

    date_registered = datetime.strptime(date_registered, "%a, %d %b %Y %H:%M:%S GMT").date()

    # Create user and add to db
    new_user = User(username=username, email=email, subscription_id=subscription_id, date_registered=date_registered, location=location, status=status)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': f'User successfully created', 'username': username, 'subscription_id': subscription_id}), 201

@main_bp.route('/user/<int:id>', methods=['GET'])
def get_user():
    return jsonify({'message': 'Not implemented'}), 405

@main_bp.route('/user/<int:id>', methods=['PUT'])
def update_user():
    return jsonify({'message': 'Not implemented'}), 405

@main_bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user():
    return jsonify({'message' : 'Not implemented'}), 405
