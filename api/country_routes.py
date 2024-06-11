from flask import Blueprint, jsonify
from app.models import Country

country_routes = Blueprint('country_routes', __name__)

@country_routes.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    return jsonify([country.serialize() for country in countries]), 200

@country_routes.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = Country.query.filter_by(code=country_code).first()
    if country:
        return jsonify(country.serialize()), 200
    else:
        return jsonify({"error": "Country not found"}), 404
