import unittest
import json
from flask import Flask
from api.routes import app as general_app
from api.user_api import user_app

class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(general_app)
        self.app.register_blueprint(user_app, url_prefix='/api/v1')
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users', data=json.dumps({
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_users(self):
        response = self.client.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get_user(self):
        # Create a user first
        post_response = self.client.post('/api/v1/users', data=json.dumps({
            'email': 'test2@example.com',
            'first_name': 'Jane',
            'last_name': 'Doe'
        }), content_type='application/json')
        user_id = json.loads(post_response.data)['id']

        # Get the user by ID
        get_response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertIn('email', json.loads(get_response.data))

    def test_update_user(self):
        # Create a user first
        post_response = self.client.post('/api/v1/users', data=json.dumps({
            'email': 'test3@example.com',
            'first_name': 'Alice',
            'last_name': 'Doe'
        }), content_type='application/json')
        user_id = json.loads(post_response.data)['id']

        # Update the user's first name
        put_response = self.client.put(f'/api/v1/users/{user_id}', data=json.dumps({
            'first_name': 'Alicia'
        }), content_type='application/json')
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(json.loads(put_response.data)['first_name'], 'Alicia')

    def test_delete_user(self):
        # Create a user first
        post_response = self.client.post('/api/v1/users', data=json.dumps({
            'email': 'test4@example.com',
            'first_name': 'Bob',
            'last_name': 'Doe'
        }), content_type='application/json')
        user_id = json.loads(post_response.data)['id']

        # Delete the user by ID
        delete_response = self.client.delete(f'/api/v1/users/{user_id}')
        self.assertEqual(delete_response.status_code, 204)

        # Verify the user has been deleted
        get_response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
