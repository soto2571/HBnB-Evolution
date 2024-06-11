from flask import Blueprint, jsonify, request
from app.models import Place

place_routes = Blueprint('place_routes', __name__)

# Dummy data for demonstration
example_places = [
    {
        "id": 1,
        "name": "Cozy Apartment",
        "description": "A comfortable apartment in the heart of the city.",
        "address": "123 Main Street",
        "city_id": 1,
        "latitude": 40.7128,
        "longitude": -74.0060,
        "host_id": 1,
        "number_of_rooms": 2,
        "number_of_bathrooms": 1,
        "price_per_night": 100,
        "max_guests": 4,
        "amenity_ids": [1, 2]
    },
    {
        "id": 2,
        "name": "Luxury Villa",
        "description": "A luxurious villa with a stunning view.",
        "address": "456 Elm Street",
        "city_id": 2,
        "latitude": 34.0522,
        "longitude": -118.2437,
        "host_id": 2,
        "number_of_rooms": 4,
        "number_of_bathrooms": 3,
        "price_per_night": 500,
        "max_guests": 10,
        "amenity_ids": [2, 3, 4]
    }
]

@place_routes.route('/places', methods=['GET'])
def get_places():
    return jsonify(example_places), 200

@place_routes.route('/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = next((place for place in example_places if place["id"] == place_id), None)
    if place:
        return jsonify(place), 200
    else:
        return jsonify({"error": "Place not found"}), 404

@place_routes.route('/places', methods=['POST'])
def create_place():
    data = request.json
    # Implement validation and data handling here
    new_place = {
        "id": len(example_places) + 1,
        "name": data.get('name'),
        "description": data.get('description'),
        # Include other fields here...
    }
    example_places.append(new_place)
    return jsonify(new_place), 201

@place_routes.route('/places/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.json
    place = next((place for place in example_places if place["id"] == place_id), None)
    if not place:
        return jsonify({"error": "Place not found"}), 404
    # Implement update logic here
    return jsonify(place), 200

@place_routes.route('/places/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    global example_places
    example_places = [place for place in example_places if place["id"] != place_id]
    return jsonify({}), 204

