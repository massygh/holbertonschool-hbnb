#!/usr/bin/python3
import unittest
from model.city import City  # Assure-toi d'importer correctement la classe City
import uuid
from datetime import datetime

class TestCity(unittest.TestCase):

    def test_creation_city(self):
        # Créer une instance valide de City
        city_name = "Paris"
        country_id = "country123"
        city = City(city_name, country_id)

        # Vérifier si l'instance a été créée avec les attributs corrects
        self.assertEqual(city.name, city_name)
        self.assertEqual(city.country_id, country_id)

        # Vérifier si l'ID de la ville est une chaîne UUID valide
        self.assertTrue(uuid.UUID(city.city_id))

        # Vérifier si les horodatages de création et de mise à jour sont définis
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_to_dict(self):
        # Créer une instance de City
        city = City("New York", "country456")

        # Appeler la méthode to_dict
        city_dict = city.to_dict()

        # Vérifier si la méthode to_dict renvoie un dictionnaire avec les clés et les valeurs correctes
        self.assertIsInstance(city_dict, dict)
        self.assertIn('city_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertIn('country_id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertEqual(city_dict['name'], city.name)
        self.assertEqual(city_dict['city_id'], city.city_id)
        self.assertEqual(city_dict['country_id'], city.country_id)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()