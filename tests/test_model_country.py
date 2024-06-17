#!/usr/bin/python3

import unittest
from datetime import datetime
from model.country import Country  # Assure-toi d'importer correctement la classe Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        # Créer une instance de Country pour une utilisation dans les tests
        self.country = Country("France")

    def test_creation_country(self):
        # Vérifier que le country a été créé avec le nom correct
        self.assertEqual(self.country.name, "France")

        # Vérifier que le country a un identifiant non vide
        self.assertTrue(self.country.country_id)

        # Vérifier que les horodatages de création et de mise à jour sont définis et qu'ils sont proches dans le temps
        self.assertIsInstance(self.country.created_at, datetime)
        self.assertIsInstance(self.country.updated_at, datetime)
        self.assertAlmostEqual((self.country.updated_at - self.country.created_at).total_seconds(), 0, delta=1)

    def test_to_dict(self):
        # Vérifier que la méthode to_dict renvoie un dictionnaire contenant les bonnes clés
        country_dict = self.country.to_dict()
        self.assertIsInstance(country_dict, dict)
        self.assertIn('country_id', country_dict)
        self.assertIn('name', country_dict)
        self.assertIn('created_at', country_dict)
        self.assertIn('updated_at', country_dict)

        # Vérifier que les valeurs du dictionnaire correspondent aux attributs du country
        self.assertEqual(country_dict['name'], self.country.name)
        self.assertEqual(country_dict['country_id'], self.country.country_id)
        self.assertEqual(country_dict['created_at'], self.country.created_at.isoformat())
        self.assertEqual(country_dict['updated_at'], self.country.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()