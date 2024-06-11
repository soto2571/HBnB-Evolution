from flask import Blueprint, request, jsonify
from app.models import City
from app import db

city_routes = Blueprint('city_routes', __name__)

@city_routes.route('/cities', methods=['GET'])
def get_cities():
    cities = City.query.all()
    return jsonify([city.serialize() for city in cities]), 200

@city_routes.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = City.query.get(city_id)
    if city:
        return jsonify(city.serialize()), 200
    else:
        return jsonify({"error": "City not found"}), 404

@city_routes.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    city = City(name=data['name'], country_code=data['country_code'])
    db.session.add(city)
    db.session.commit()
    return jsonify({"message": "City created successfully"}), 201

@city_routes.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    city = City.query.get(city_id)
    if city:
        data = request.json
        city.name = data.get('name', city.name)
        city.country_code = data.get('country_code', city.country_code)
        db.session.commit()
        return jsonify({"message": "City updated successfully"}), 200
    else:
        return jsonify({"error": "City not found"}), 404

@city_routes.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.query.get(city_id)
    if city:
        db.session.delete(city)
        db.session.commit()
        return jsonify({"message": "City deleted successfully"}), 204
    else:
        return jsonify({"error": "City not found"}), 404
