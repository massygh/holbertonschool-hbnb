from flask import Blueprint, request, jsonify, abort
from persistence.DataManager import DataManager
from models.city import City

# Create a Blueprint for the country and city API
country_city_app = Blueprint('country_city_app', __name__)

# Initialize DataManager
data_manager = DataManager()

# Helper function to validate country code
def validate_country_code(country_code):
    return data_manager.get(country_code, 'Country') is not None

# Retrieve all countries
@country_city_app.route('/countries', methods=['GET'])
def get_countries():
    countries = data_manager.get_all('Country')
    return jsonify([country.to_dict() for country in countries]), 200

# Retrieve details of a specific country by its code
@country_city_app.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = data_manager.get(country_code, 'Country')
    if country:
        return jsonify(country.to_dict()), 200
    else:
        abort(404, description="Country not found")

# Retrieve all cities belonging to a specific country
@country_city_app.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    if not validate_country_code(country_code):
        abort(404, description="Country not found")
    
    cities = [city.to_dict() for city in data_manager.get_all('City') if city.country_code == country_code]
    return jsonify(cities), 200

# Create a new city
@country_city_app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "country_code")):
        abort(400, description="Missing required fields")
    if not validate_country_code(data['country_code']):
        abort(400, description="Invalid country code")

    city = City(name=data['name'], country_code=data['country_code'])
    if data_manager.save(city):
        return jsonify(city.to_dict()), 201
    else:
        abort(409, description="City creation failed")

# Retrieve all cities
@country_city_app.route('/cities', methods=['GET'])
def get_cities():
    cities = data_manager.get_all('City')
    return jsonify([city.to_dict() for city in cities]), 200

# Retrieve details of a specific city
@country_city_app.route('/cities/<uuid:city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get(city_id, 'City')
    if city:
        return jsonify(city.to_dict()), 200
    else:
        abort(404, description="City not found")

# Update an existing city’s information
@country_city_app.route('/cities/<uuid:city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    if not data:
        abort(400, description="Missing required fields")

    city = data_manager.get(city_id, 'City')
    if not city:
        abort(404, description="City not found")

    if 'country_code' in data and not validate_country_code(data['country_code']):
        abort(400, description="Invalid country code")

    city.update(name=data.get('name'), country_code=data.get('country_code'))
    updated_city = data_manager.update(city)
    return jsonify(updated_city.to_dict()), 200

# Delete a specific city
@country_city_app.route('/cities/<uuid:city_id>', methods=['DELETE'])
def delete_city(city_id):
    if data_manager.delete(city_id, 'City'):
        return '', 204
    else:
        abort(404, description="City not found")
