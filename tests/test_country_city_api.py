import unittest
import json
from flask import Flask
from api.country_city_api import country_city_app

class CountryCityApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(country_city_app, url_prefix='/api/v1')
        self.client = self.app.test_client()

    def test_get_countries(self):
        response = self.client.get('/api/v1/countries')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get_country(self):
        response = self.client.get('/api/v1/countries/US')
        self.assertEqual(response.status_code, 200)
        self.assertIn('code', json.loads(response.data))
        self.assertIn('name', json.loads(response.data))

    def test_get_cities_by_country(self):
        response = self.client.get('/api/v1/countries/US/cities')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_create_city(self):
        response = self.client.post('/api/v1/cities', data=json.dumps({
            'name': 'New York',
            'country_code': 'US'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()
