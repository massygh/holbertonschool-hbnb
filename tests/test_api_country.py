import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restx import Api
import sys
import os

# Ajouter le répertoire parent au sys.path pour que les modules puissent être importés
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.api_country import ns as countries_ns
from data_manager import DataManager

class TestCountriesAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(countries_ns)
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_countries')
    def test_get_all_countries(self, mock_get_all_countries):
        mock_countries = [
            {'id': '1', 'name': 'France', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'},
            {'id': '2', 'name': 'USA', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        ]
        mock_get_all_countries.return_value = mock_countries

        response = self.client.get('/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_countries)

    @patch.object(DataManager, 'save_country')
    def test_create_country(self, mock_save_country):
        mock_save_country.return_value = '1'
        new_country = {
            'name': 'Germany'
        }

        response = self.client.post('/countries/', json=new_country)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Country created successfully', response.json['message'])
        self.assertEqual(response.json['country_id'], '1')

    @patch.object(DataManager, 'get_country')
    def test_get_country_by_id(self, mock_get_country):
        mock_country = {'id': '1', 'name': 'France', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_get_country.return_value = mock_country

        response = self.client.get('/countries/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_country)

    @patch.object(DataManager, 'delete_country')
    def test_delete_country(self, mock_delete_country):
        mock_delete_country.return_value = True

        response = self.client.delete('/countries/1')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_country')
    @patch.object(DataManager, 'get_country')
    def test_update_country(self, mock_get_country, mock_update_country):
        mock_get_country.return_value = {'id': '1', 'name': 'France', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_update_country.return_value = True

        updated_country = {
            'name': 'Germany',
            'updated_at': '2024-06-12T12:00:00'
        }

        response = self.client.put('/countries/1', json=updated_country)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()