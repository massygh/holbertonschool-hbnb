import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restx import Api
import sys
import os

# Ajouter le répertoire parent au sys.path pour que les modules puissent être importés
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.api_review import ns as reviews_ns
from data_manager import DataManager

class TestReviewsAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(reviews_ns)
        self.client = self.app.test_client()

    @patch.object(DataManager, 'get_all_reviews')
    def test_get_all_reviews(self, mock_get_all_reviews):
        mock_reviews = [
            {'id': '1', 'user_id': 1, 'place_id': 1, 'rating': 5, 'comment': 'Excellent!', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'},
            {'id': '2', 'user_id': 2, 'place_id': 2, 'rating': 4, 'comment': 'Very good', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        ]
        mock_get_all_reviews.return_value = mock_reviews

        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_reviews)

    @patch.object(DataManager, 'save_review')
    def test_create_review(self, mock_save_review):
        mock_save_review.return_value = '1'
        new_review = {
            'user_id': 1,
            'place_id': 1,
            'rating': 5,
            'comment': 'Excellent!'
        }

        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Review created successfully', response.json['message'])
        self.assertEqual(response.json['review_id'], '1')

    @patch.object(DataManager, 'get_review')
    def test_get_review_by_id(self, mock_get_review):
        mock_review = {'id': '1', 'user_id': 1, 'place_id': 1, 'rating': 5, 'comment': 'Excellent!', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_get_review.return_value = mock_review

        response = self.client.get('/reviews/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_review)

    @patch.object(DataManager, 'delete_review')
    def test_delete_review(self, mock_delete_review):
        mock_delete_review.return_value = True

        response = self.client.delete('/reviews/1')
        self.assertEqual(response.status_code, 204)

    @patch.object(DataManager, 'update_review')
    @patch.object(DataManager, 'get_review')
    def test_update_review(self, mock_get_review, mock_update_review):
        mock_get_review.return_value = {'id': '1', 'user_id': 1, 'place_id': 1, 'rating': 5, 'comment': 'Excellent!', 'created_at': '2024-06-11T12:00:00', 'updated_at': '2024-06-11T12:00:00'}
        mock_update_review.return_value = True

        updated_review = {
            'user_id': 1,
            'place_id': 1,
            'rating': 4,
            'comment': 'Very good',
            'updated_at': '2024-06-12T12:00:00'
        }

        response = self.client.put('/reviews/1', json=updated_review)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()