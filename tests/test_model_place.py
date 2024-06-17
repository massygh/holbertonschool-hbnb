#!/usr/bin/python3

import unittest
from model.place import Place  # Assure-toi d'importer correctement la classe Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        # Créer une instance de Place pour une utilisation dans les tests
        self.place = Place(
            name="Cosy Apartment",
            description="A comfortable apartment in the city center.",
            address="123 Main St",
            city_id="123456",
            latitude=40.7128,
            longitude=-74.0060,
            host_id="host123",
            number_of_rooms=2,
            number_of_bathrooms=1,
            price_per_night=100,
            max_guests=4,
            amenity_ids=["wifi", "kitchen"]
        )

    def test_creation_place(self):
        # Vérifier que le place a été créé avec les attributs corrects
        self.assertEqual(self.place.name, "Cosy Apartment")
        self.assertEqual(self.place.description, "A comfortable apartment in the city center.")
        self.assertEqual(self.place.address, "123 Main St")
        self.assertEqual(self.place.city_id, "123456")
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.host_id, "host123")
        self.assertEqual(self.place.number_of_rooms, 2)
        self.assertEqual(self.place.number_of_bathrooms, 1)
        self.assertEqual(self.place.price_per_night, 100)
        self.assertEqual(self.place.max_guests, 4)
        self.assertEqual(self.place.amenity_ids, ["wifi", "kitchen"])
        self.assertEqual(self.place.reviews, [])

    def test_add_review(self):
        # Ajouter une critique et vérifier qu'elle est correctement ajoutée à la liste des critiques
        review = "Great place to stay!"
        self.place.add_review(review)
        self.assertIn(review, self.place.reviews)

    def test_calculate_total_price(self):
        # Vérifier que le calcul du prix total est correct pour un nombre de nuits donné
        total_price = self.place.calculate_total_price(3)
        self.assertEqual(total_price, 300)

    def test_list_amenities(self):
        # Vérifier que la liste des commodités est correctement renvoyée
        amenities = self.place.list_amenities()
        self.assertEqual(amenities, ["wifi", "kitchen"])

    # Tu peux ajouter d'autres tests pour les autres méthodes de la classe Place ici...

if __name__ == '__main__':
    unittest.main()