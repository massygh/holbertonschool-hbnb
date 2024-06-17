#!/usr/bin/python3
# API for managing cities

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager
from model.city import City
from datetime import datetime

ns = Namespace('cities', description='Operations related to cities')
data_manager = DataManager()

# Model definition for a City
city_model = ns.model('City', {
    'city_id': fields.String(
        required=True,
        description='City ID'
    ),
    'name': fields.String(
        required=True,
        description='City name'
    ),
    'country_id': fields.String(
        required=True,
        description='Country ID'
    ),
    'created_at': fields.DateTime(
        required=True,
        description='Date and time when the city was created'
    ),
    'updated_at': fields.DateTime(
        required=True,
        description='Date and time when the city was last updated'
    )
})


@ns.route('/')
class Cities(Resource):
    @ns.marshal_list_with(city_model)
    def get(self):
        """Fetch all cities."""
        return data_manager.get_all_cities()

    @ns.expect(city_model)
    @ns.response(201, 'City created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """Create a new city."""
        new_city_data = request.json
        city = City(new_city_data['name'], new_city_data['country_id'])
        data_manager.save_city(city.to_dict())
        return {
            'message': 'City created successfully',
            'city_id': city.city_id
        }, 201


@ns.route('/<string:city_id>')
class CityResource(Resource):
    @ns.marshal_with(city_model)
    @ns.response(404, 'City not found')
    def get(self, city_id):
        """Fetch a city by its ID."""
        city_data = data_manager.get_city(city_id)
        if city_data:
            return city_data
        else:
            ns.abort(404, "City not found")

    @ns.response(204, 'City deleted successfully')
    @ns.response(404, 'City not found')
    def delete(self, city_id):
        """Delete an existing city."""
        if data_manager.delete_city(city_id):
            return '', 204
        else:
            ns.abort(404, "City not found")

    @ns.expect(city_model)
    @ns.response(204, 'City updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'City not found')
    def put(self, city_id):
        """Update an existing city."""
        new_city_data = request.json
        new_city_data['city_id'] = city_id
        new_city_data['updated_at'] = datetime.now().isoformat()
        if data_manager.update_city(city_id, new_city_data):
            return '', 204
        else:
            ns.abort(404, "City not found")
