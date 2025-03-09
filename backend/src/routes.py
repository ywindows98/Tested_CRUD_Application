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
    users = User.query.all()
    if users:
        user_dicts = [user.to_dict() for user in users]

        for i in range(len(user_dicts)):
            user_dicts[i]['status'] = user_dicts[i]['status'].name

        return jsonify(user_dicts), 200

    return jsonify({'message': 'No users found'}), 404

@main_bp.route('/user', methods=['POST'])
def create_user():
    """
    Method to handle new user creation.

    Method expects a JSON payload containing user data.

    Expected JSON payload:
    {
        'username': 'string', - REQUIRED
        'email': 'string', - REQUIRED
        'subscription_id': 'int', - REQUIRED
        'date_registered': 'string' - datetime.datetime format
        'location': 'string',
        'status': 'string'
    }

    If any of the required values is missing, a 400 Bad Request response will be returned.
    The new user will be added to the database if the validation is successful.

    :return:
        JSON response with a message or an error and a status code.
    """

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

    if username is None:
        return jsonify({'error': f'No given username for creation'}), 400

    if email is None:
        return jsonify({'error': f'No given email for creation'}), 400

    if subscription_id is None:
        return jsonify({'error': f'No given subscription_id for creation'}), 400

    # Create user
    new_user = User(username=username, email=email, subscription_id=subscription_id, location=location, status=status)

    # Case when date is given
    if date_registered is not None:
        date_registered = datetime.strptime(date_registered, "%a, %d %b %Y %H:%M:%S GMT").date()
        new_user.date_registered = date_registered

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': f'User successfully created'}), 201


@main_bp.route('/user/<int:id>', methods=['GET'])
def get_user():
    return jsonify({'message': 'Not implemented'}), 405

@main_bp.route('/user/<int:id>', methods=['PUT'])
def update_user():
    return jsonify({'message': 'Not implemented'}), 405

@main_bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user():
    return jsonify({'message' : 'Not implemented'}), 405
