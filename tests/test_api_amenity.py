#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restx import Api
import sys
import os

# Ajouter le répertoire parent au sys.path pour que les modules puissent être importés
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.api_amenity import ns as amenities_ns
from data_manager import DataManager

class TestAmenitiesAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(amenities_ns)
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_amenities')
    def test_get_all_amenities(self, mock_get_all_amenities):
        mock_amenities = [
            {'id': '1', 'name': 'Pool', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'},
            {'id': '2', 'name': 'WiFi', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        ]
        mock_get_all_amenities.return_value = mock_amenities

        response = self.client.get('/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_amenities)

    @patch.object(DataManager, 'save_amenity')
    def test_create_amenity(self, mock_save_amenity):
        mock_save_amenity.return_value = '1'
        new_amenity = {
            'name': 'Gym'
        }

        response = self.client.post('/amenities/', json=new_amenity)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Amenity created successfully', response.json['message'])
        self.assertEqual(response.json['amenity_id'], '1')

    @patch.object(DataManager, 'get_amenity')
    def test_get_amenity_by_id(self, mock_get_amenity):
        mock_amenity = {'id': '1', 'name': 'Pool', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_get_amenity.return_value = mock_amenity

        response = self.client.get('/amenities/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_amenity)

    @patch.object(DataManager, 'delete_amenity')
    def test_delete_amenity(self, mock_delete_amenity):
        mock_delete_amenity.return_value = True

        response = self.client.delete('/amenities/1')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_amenity')
    def test_update_amenity(self, mock_update_amenity):
        mock_update_amenity.return_value = True
        updated_amenity = {
            'name': 'Updated Gym'
        }

        response = self.client.put('/amenities/1', json=updated_amenity)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()