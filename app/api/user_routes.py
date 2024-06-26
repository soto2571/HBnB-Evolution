from flask import Blueprint, request, jsonify
from app.persistence.data_manager import DataManager

# Create a Blueprint for user routes
user_routes = Blueprint('user_routes', __name__)

# Instantiate DataManager
data_manager = DataManager()

# Endpoint for creating a new user
@user_routes.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    # Perform input validation
    if 'email' not in user_data or 'first_name' not in user_data or 'last_name' not in user_data:
        return jsonify({'error': 'Missing required fields'}), 400
    # Validate email format and uniqueness
    # Add user to the database
    user_id = data_manager.create_user(user_data)
    return jsonify({'user_id': user_id}), 201

# Endpoint for retrieving all users
@user_routes.route('/users', methods=['GET'])
def get_all_users():
    users = data_manager.get_all_users()
    return jsonify(users), 200

# Endpoint for retrieving a specific user
@user_routes.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get_user(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200

# Endpoint for updating an existing user
@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    # Perform input validation
    # Update user in the database
    success = data_manager.update_user(user_id, user_data)
    if not success:
        return jsonify({'error': 'User not found'}), 404
    return '', 204

# Endpoint for deleting a user
@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = data_manager.delete_user(user_id)
    if not success:
        return jsonify({'error': 'User not found'}), 404
    return '', 204
