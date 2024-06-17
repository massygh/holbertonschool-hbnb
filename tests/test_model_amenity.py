#!/usr/bin/python3
import unittest
from model.amenity import Amenity  # Assure-toi d'importer correctement la classe Amenity
import uuid
from datetime import datetime

class TestAmenity(unittest.TestCase):

    def test_creation_amenity(self):
        # Créer une instance valide d'Amenity
        amenity_name = "Swimming Pool"
        amenity = Amenity(amenity_name)

        # Vérifier si l'instance a été créée avec les attributs corrects
        self.assertEqual(amenity.name, amenity_name)

        # Vérifier si l'ID d'amenity est une chaîne UUID valide
        self.assertTrue(uuid.UUID(amenity.amenity_id))

        # Vérifier si les horodatages de création et de mise à jour sont définis
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_to_dict(self):
        # Créer une instance d'Amenity
        amenity = Amenity("Gym")

        # Appeler la méthode to_dict
        amenity_dict = amenity.to_dict()

        # Vérifier si la méthode to_dict renvoie un dictionnaire avec les clés et les valeurs correctes
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('amenity_id', amenity_dict)
        self.assertIn('name', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['name'], amenity.name)
        self.assertEqual(amenity_dict['amenity_id'], amenity.amenity_id)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()