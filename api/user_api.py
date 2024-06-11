from flask import Blueprint, request, jsonify, abort
from persistence.DataManager import DataManager
from models.user import User
import re
import uuid

# Create a Blueprint for the user API
user_app = Blueprint('user_app', __name__)

# Initialize DataManager
data_manager = DataManager()

# Helper function to validate email format
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Create a new user
@user_app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ("email", "first_name", "last_name")):
        abort(400, description="Missing required fields")
    if not validate_email(data['email']):
        abort(400, description="Invalid email format")
    
    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'], password="")
    if data_manager.save(user):
        return jsonify(user.to_dict()), 201
    else:
        abort(409, description="User with this email already exists")

# Retrieve all users
@user_app.route('/users', methods=['GET'])
def get_users():
    users = data_manager.get_all("User")
    return jsonify([user.to_dict() for user in users]), 200

# Retrieve a specific user by ID
@user_app.route('/users/<uuid:user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, "User")
    if user:
        return jsonify(user.to_dict()), 200
    else:
        abort(404, description="User not found")

# Update an existing user by ID
@user_app.route('/users/<uuid:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data or not any(k in data for k in ("email", "first_name", "last_name")):
        abort(400, description="Missing required fields")
    user = data_manager.get(user_id, "User")
    if not user:
        abort(404, description="User not found")

    if 'email' in data and not validate_email(data['email']):
        abort(400, description="Invalid email format")

    user.update(email=data.get('email'), first_name=data.get('first_name'), last_name=data.get('last_name'))
    updated_user = data_manager.update(user)
    return jsonify(updated_user.to_dict()), 200

# Delete a user by ID
@user_app.route('/users/<uuid:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if data_manager.delete(user_id, "User"):
        return '', 204
    else:
        abort(404, description="User not found")
