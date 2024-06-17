import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restx import Api
import sys
import os

# Ajouter le répertoire parent au sys.path pour que les modules puissent être importés
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.api_user import ns as users_ns
from data_manager import DataManager

class TestUsersAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(users_ns)
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_users')
    def test_get_all_users(self, mock_get_all_users):
        mock_users = [
            {'id': '1', 'username': 'user1', 'email': 'user1@example.com', 'password': 'password', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'},
            {'id': '2', 'username': 'user2', 'email': 'user2@example.com', 'password': 'password', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        ]
        mock_get_all_users.return_value = mock_users

        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_users)

    @patch.object(DataManager, 'save_user')
    def test_create_user(self, mock_save_user):
        mock_save_user.return_value = '1'
        new_user = {
            'username': 'user3',
            'email': 'user3@example.com',
            'password': 'password'
        }

        response = self.client.post('/users/', json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created successfully', response.json['message'])
        self.assertEqual(response.json['user_id'], '1')

    @patch.object(DataManager, 'get_user')
    def test_get_user_by_id(self, mock_get_user):
        mock_user = {'id': '1', 'username': 'user1', 'email': 'user1@example.com', 'password': 'password', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_get_user.return_value = mock_user

        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_user)

    @patch.object(DataManager, 'delete_user')
    def test_delete_user(self, mock_delete_user):
        mock_delete_user.return_value = True

        response = self.client.delete('/users/1')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_user')
    @patch.object(DataManager, 'get_user')
    def test_update_user(self, mock_get_user, mock_update_user):
        mock_get_user.return_value = {'id': '1', 'username': 'user1', 'email': 'user1@example.com', 'password': 'password', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_update_user.return_value = True

        updated_user = {
            'username': 'updated_user1',
            'email': 'updated_user1@example.com',
            'password': 'new_password',
            'updated_at': '2024-06-12T12:00:00'
        }

        response = self.client.put('/users/1', json=updated_user)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()