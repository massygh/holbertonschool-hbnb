from flask import Blueprint, request, jsonify, abort
from persistence.DataManager import DataManager
from models.amenity import Amenity

# Create a Blueprint for the amenity API
amenity_app = Blueprint('amenity_app', __name__)

# Initialize DataManager
data_manager = DataManager()

# Create a new amenity
@amenity_app.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    if not data or not 'name' in data:
        abort(400, description="Missing required fields")
    
    amenity = Amenity(name=data['name'])
    if data_manager.save(amenity):
        return jsonify(amenity.to_dict()), 201
    else:
        abort(409, description="Amenity with this name already exists")

# Retrieve all amenities
@amenity_app.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = data_manager.get_all('Amenity')
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

# Retrieve details of a specific amenity
@amenity_app.route('/amenities/<uuid:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity:
        return jsonify(amenity.to_dict()), 200
    else:
        abort(404, description="Amenity not found")

# Update an existing amenity’s information
@amenity_app.route('/amenities/<uuid:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    if not data or not 'name' in data:
        abort(400, description="Missing required fields")

    amenity = data_manager.get(amenity_id, 'Amenity')
    if not amenity:
        abort(404, description="Amenity not found")

    amenity.update(name=data['name'])
    updated_amenity = data_manager.update(amenity)
    return jsonify(updated_amenity.to_dict()), 200

# Delete a specific amenity
@amenity_app.route('/amenities/<uuid:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    if data_manager.delete(amenity_id, 'Amenity'):
        return '', 204
    else:
        abort(404, description="Amenity not found")
