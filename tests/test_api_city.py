import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restx import Api
import sys
import os

# Ajouter le répertoire parent au sys.path pour que les modules puissent être importés
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.api_city import ns as cities_ns
from data_manager import DataManager

class TestCitiesAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(cities_ns)
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_cities')
    def test_get_all_cities(self, mock_get_all_cities):
        mock_cities = [
            {'id': '1', 'name': 'Paris', 'country_id': 1, 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'},
            {'id': '2', 'name': 'New York', 'country_id': 2, 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        ]
        mock_get_all_cities.return_value = mock_cities

        response = self.client.get('/cities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_cities)

    @patch.object(DataManager, 'save_city')
    def test_create_city(self, mock_save_city):
        mock_save_city.return_value = '1'
        new_city = {
            'name': 'Los Angeles',
            'country_id': 3
        }

        response = self.client.post('/cities/', json=new_city)
        self.assertEqual(response.status_code, 201)
        self.assertIn('City created successfully', response.json['message'])
        self.assertEqual(response.json['city_id'], '1')

    @patch.object(DataManager, 'get_city')
    def test_get_city_by_id(self, mock_get_city):
        mock_city = {'id': '1', 'name': 'Paris', 'country_id': 1, 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_get_city.return_value = mock_city

        response = self.client.get('/cities/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_city)

    @patch.object(DataManager, 'delete_city')
    def test_delete_city(self, mock_delete_city):
        mock_delete_city.return_value = True

        response = self.client.delete('/cities/1')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_city')
    @patch.object(DataManager, 'get_city')
    def test_update_city(self, mock_get_city, mock_update_city):
        mock_get_city.return_value = {'id': '1', 'name': 'Paris', 'country_id': 1, 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_update_city.return_value = True

        updated_city = {
            'id': '1',
            'name': 'San Francisco',
            'country_id': 1,
            'created_at': '2024-06-11T12:00:00',
            'updated_at': '2024-06-11T12:00:00'
        }

        response = self.client.put('/cities/1', json=updated_city)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()