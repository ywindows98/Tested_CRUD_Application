from flask import Blueprint, jsonify
from .models import User
from .database import db

main_bp = Blueprint('main', __name__)  # Create a blueprint

@main_bp.route('/')
def home():
    return jsonify({'message': 'Home page'})

@main_bp.route('/user', methods=['GET'])
def get_users():
    return jsonify({'message' : 'Not implemented'}), 405

@main_bp.route('/user', methods=['POST'])
def create_user():
    return jsonify({'message' : 'Not implemented'}), 405

@main_bp.route('/user/<int:id>', methods=['GET'])
def get_user():
    return jsonify({'message' : 'Not implemented'}), 405

@main_bp.route('/user/<int:id>', methods=['PUT'])
def update_user():
    return jsonify({'message' : 'Not implemented'}), 405

@main_bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user():
    return jsonify({'message' : 'Not implemented'}), 405
