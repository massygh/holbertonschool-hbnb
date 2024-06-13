import unittest
import json
from flask import Flask
from api.amenity_api import amenity_app

class AmenityApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(amenity_app, url_prefix='/api/v1')
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_amenities(self):
        response = self.client.get('/api/v1/amenities')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get_amenity(self):
        post_response = self.client.post('/api/v1/amenities', data=json.dumps({
            'name': 'Swimming Pool'
        }), content_type='application/json')
        amenity_id = json.loads(post_response.data)['id']

        get_response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertIn('name', json.loads(get_response.data))

    def test_update_amenity(self):
        post_response = self.client.post('/api/v1/amenities', data=json.dumps({
            'name': 'Parking'
        }), content_type='application/json')
        amenity_id = json.loads(post_response.data)['id']

        put_response = self.client.put(f'/api/v1/amenities/{amenity_id}', data=json.dumps({
            'name': 'Free Parking'
        }), content_type='application/json')
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(json.loads(put_response.data)['name'], 'Free Parking')

    def test_delete_amenity(self):
        post_response = self.client.post('/api/v1/amenities', data=json.dumps({
            'name': 'Gym'
        }), content_type='application/json')
        amenity_id = json.loads(post_response.data)['id']

        delete_response = self.client.delete(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(delete_response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
