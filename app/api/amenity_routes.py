from flask import Blueprint, jsonify, request
from app.models import Amenity

amenity_routes = Blueprint('amenity_routes', __name__)

# Dummy data for demonstration
example_amenities = [
    {"id": 1, "name": "Wi-Fi"},
    {"id": 2, "name": "Swimming Pool"},
]

@amenity_routes.route('/amenities', methods=['GET'])
def get_amenities():
    return jsonify(example_amenities), 200

@amenity_routes.route('/amenities/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = next((amenity for amenity in example_amenities if amenity["id"] == amenity_id), None)
    if amenity:
        return jsonify(amenity), 200
    else:
        return jsonify({"error": "Amenity not found"}), 404

@amenity_routes.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    existing_amenity = next((amenity for amenity in example_amenities if amenity["name"] == name), None)
    if existing_amenity:
        return jsonify({"error": "Amenity with this name already exists"}), 409
    
    new_amenity = {
        "id": len(example_amenities) + 1,
        "name": name
    }
    example_amenities.append(new_amenity)
    
    return jsonify(new_amenity), 201

@amenity_routes.route('/amenities/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.json
    name = data.get('name')
    
    amenity = next((amenity for amenity in example_amenities if amenity["id"] == amenity_id), None)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    
    existing_amenity = next((amenity for amenity in example_amenities if amenity["name"] == name), None)
    if existing_amenity and existing_amenity["id"] != amenity_id:
        return jsonify({"error": "Amenity with this name already exists"}), 409
    
    amenity["name"] = name if name else amenity["name"]
    
    return jsonify(amenity), 200

@amenity_routes.route('/amenities/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    global example_amenities
    example_amenities = [amenity for amenity in example_amenities if amenity["id"] != amenity_id]
    return jsonify({}), 204
