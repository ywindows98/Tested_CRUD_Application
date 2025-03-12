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
    """
    Method to handle user reading.

    Method queries all users from db, serializes them to json and returns.
    If there are no users in the db, response code is 404.

    :return:
        JSON list of user dictionaries and a response code 200.
    """
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
def get_user(id):
    """
    Method to handle specific user reading.
    Method queries a user from a database by an id.
    If there is no user with given id in the database the response is 404.

    :return:
        JSON dictionary of user and a response code 200.
    """
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': f'No user with id={id} found'}), 404

    user_dict = user.to_dict()
    user_dict['status'] = user_dict['status'].name

    return jsonify(user_dict), 200



@main_bp.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Method to handle user updating.
    
    Method expects a JSON payload containing updated user data.
    
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
    User will be updated in the database if the validation is successful.
    
    :return:
        JSON response with a message or an error and a status code.
    """
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': f'No user with id={id} found'}), 404

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
        return jsonify({'error': f'No given username in update'}), 400

    if email is None:
        return jsonify({'error': f'No given email in update'}), 400

    if subscription_id is None:
        return jsonify({'error': f'No given subscription_id in update'}), 400

     # Case when date is given
    if date_registered is not None:
        date_registered = datetime.strptime(date_registered, "%a, %d %b %Y %H:%M:%S GMT").date()

    # Update user
    user.username = username
    user.email = email
    user.subscription_id = subscription_id
    if 'date_registered' in data:
        user.date_registered = date_registered
    user.location = location
    if 'date_registered' in data:
        user.status = status

    db.session.commit()

    return jsonify({'message': f'User successfully updated'}), 200

@main_bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    return jsonify({'message' : 'Not implemented'}), 405
