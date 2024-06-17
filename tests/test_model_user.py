#!/usr/bin/python3

import unittest
from model.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        # Créer une instance de User pour une utilisation dans les tests
        self.user = User(
            username="john_doe",
            email="john@example.com",
            password="password123"
        )

    def test_creation_user(self):
        # Vérifie que le user a été créé avec les attributs corrects
        self.assertTrue(self.user.user_id)
        self.assertEqual(self.user.username, "john_doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.password, "password123")

        # Vérifier que les horodatages de création et de mise à
        # jour sont définis et qu'ils sont proches dans le temps
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
        self.assertAlmostEqual(
            (self.user.updated_at - self.user.created_at).total_seconds(),
            0, delta=1)

    def test_add_review(self):
        # Ajouter une critique et vérifier qu'elle est
        # correctement ajoutée à la liste des critiques
        review = {"review_id": "review123", "rating": 5,
                  "comment": "Great experience!"}
        self.user.add_review(review)
        self.assertIn(review, self.user.reviews)

    def test_to_dict(self):
        # Vérifier que la méthode to_dict renvoie
        # un dictionnaire contenant les bonnes clés
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('user_id', user_dict)
        self.assertIn('username', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('reviews', user_dict)

        # Vérifier que les valeurs du dictionnaire
        # correspondent aux attributs du user
        self.assertEqual(user_dict['username'], self.user.username)
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['user_id'], self.user.user_id)
        self.assertEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'],
                         self.user.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()