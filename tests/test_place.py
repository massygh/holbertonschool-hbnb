import unittest
from model.place import Place
from model.user import User

class TestPlace(unittest.TestCase):
    def test_create_place(self):
        host = User(user_id=1, email='host@example.com', name='Host User')
        place = Place(place_id=1, host=host, name='Test Place', location='Test Location')
        self.assertEqual(place.name, 'Test Place')

    def test_add_amenity(self):
        host = User(user_id=1, email='host@example.com', name='Host User')
        place = Place(place_id=1, host=host, name='Test Place', location='Test Location')
        place.add_amenity('WiFi')
        self.assertIn('WiFi', place.amenities)

if __name__ == '__main__':
    unittest.main()