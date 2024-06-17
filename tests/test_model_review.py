#!/usr/bin/python3

import unittest
from model.review import Review  # Assure-toi d'importer correctement la classe Review

class TestReview(unittest.TestCase):

    def setUp(self):
        # Créer une instance de Review pour une utilisation dans les tests
        self.review = Review(
            user_id="user123",
            place_id="place456",
            rating=5,
            comment="Great experience!"
        )

    def test_creation_review(self):
        # Vérifier que le review a été créé avec les attributs corrects
        self.assertTrue(self.review.review_id)
        self.assertEqual(self.review.user_id, "user123")
        self.assertEqual(self.review.place_id, "place456")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great experience!")

        # Vérifier que les horodatages de création et de mise à jour sont définis et qu'ils sont proches dans le temps
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)
        self.assertAlmostEqual((self.review.updated_at - self.review.created_at).total_seconds(), 0, delta=1)

    def test_to_dict(self):
        # Vérifier que la méthode to_dict renvoie un dictionnaire contenant les bonnes clés
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('review_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('rating', review_dict)
        self.assertIn('comment', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

        # Vérifier que les valeurs du dictionnaire correspondent aux attributs du review
        self.assertEqual(review_dict['user_id'], self.review.user_id)
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['rating'], self.review.rating)
        self.assertEqual(review_dict['comment'], self.review.comment)

if __name__ == '__main__':
    unittest.main()