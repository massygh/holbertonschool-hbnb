import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restx import Api
import sys
import os

# Ajouter le répertoire parent au sys.path pour que les modules puissent être importés
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.api_place import ns as places_ns
from data_manager import DataManager

class TestPlacesAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(places_ns)
        self.client = self.app.test_client()
        self.maxDiff = None  # Pour voir les différences complètes

    @patch.object(DataManager, 'get_all_places')
    def test_get_all_places(self, mock_get_all_places):
        mock_places = [
            {
                'id': '1', 'name': 'Eiffel Tower', 'description': None, 'address': None,
                'city_id': None, 'latitude': None, 'longitude': None, 'host_id': None,
                'number_of_rooms': None, 'number_of_bathrooms': None, 'price_per_night': None,
                'max_guests': None, 'amenity_ids': None, 'created_at': '2024-06-11T12:00:00',
                'updated_at': '2024-06-11T12:00:00'
            },
            {
                'id': '2', 'name': 'Statue of Liberty', 'description': None, 'address': None,
                'city_id': None, 'latitude': None, 'longitude': None, 'host_id': None,
                'number_of_rooms': None, 'number_of_bathrooms': None, 'price_per_night': None,
                'max_guests': None, 'amenity_ids': None, 'created_at': '2024-06-11T12:00:00',
                'updated_at': '2024-06-11T12:00:00'
            }
        ]
        mock_get_all_places.return_value = mock_places

        response = self.client.get('/places/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_places)

    @patch.object(DataManager, 'save_place')
    def test_create_place(self, mock_save_place):
        mock_save_place.return_value = '1'
        new_place = {
            'name': 'Disneyland',
            'description': 'A magical place',
            'address': 'Anaheim, CA',
            'city_id': 1,
            'latitude': 33.8121,
            'longitude': -117.9190,
            'host_id': 1,
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 200.00,
            'max_guests': 5,
            'amenity_ids': ['1', '2']
        }

        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Place created successfully', response.json['message'])
        self.assertEqual(response.json['place_id'], '1')

    @patch.object(DataManager, 'get_place')
    def test_get_place_by_id(self, mock_get_place):
        mock_place = {
            'id': '1', 'name': 'Eiffel Tower', 'description': None, 'address': None,
            'city_id': None, 'latitude': None, 'longitude': None, 'host_id': None,
            'number_of_rooms': None, 'number_of_bathrooms': None, 'price_per_night': None,
            'max_guests': None, 'amenity_ids': None, 'created_at': '2024-06-11T12:00:00',
            'updated_at': '2024-06-11T12:00:00'
        }
        mock_get_place.return_value = mock_place

        response = self.client.get('/places/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_place)

    @patch.object(DataManager, 'delete_place')
    def test_delete_place(self, mock_delete_place):
        mock_delete_place.return_value = True

        response = self.client.delete('/places/1')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_place')
    @patch.object(DataManager, 'get_place')
    def test_update_place(self, mock_get_place, mock_update_place):
        mock_get_place.return_value = {
            'id': '1', 'name': 'Eiffel Tower', 'description': None, 'address': None,
            'city_id': None, 'latitude': None, 'longitude': None, 'host_id': None,
            'number_of_rooms': None, 'number_of_bathrooms': None, 'price_per_night': None,
            'max_guests': None, 'amenity_ids': None, 'created_at': '2024-06-11T12:00:00',
            'updated_at': '2024-06-11T12:00:00'
        }
        mock_update_place.return_value = True

        updated_place = {
            'name': 'Louvre Museum',
            'description': 'World famous museum',
            'address': 'Paris, France',
            'city_id': 1,
            'latitude': 48.8606,
            'longitude': 2.3376,
            'host_id': 1,
            'number_of_rooms': 10,
            'number_of_bathrooms': 5,
            'price_per_night': 300.00,
            'max_guests': 10,
            'amenity_ids': ['1', '2'],
            'updated_at': '2024-06-12T12:00:00'
        }

        response = self.client.put('/places/1', json=updated_place)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()