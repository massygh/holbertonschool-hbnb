import unittest
from models.place import Place
from models.user import User

class TestPlace(unittest.TestCase):
    def test_create_place(self):
        host = User(email='host@example.com', first_name='Host', last_name='User', password='password')
        place = Place(name='My Place', description='A nice place', address='123 Street', city_id=1, host_id=host.id, 
                      price_per_night=100, latitude=40.7128, longitude=-74.0060, number_of_rooms=3, number_of_bathrooms=2, max_guests=4)
        self.assertEqual(place.name, 'My Place')

    def test_add_amenity(self):
        host = User(email='host@example.com', first_name='Host', last_name='User', password='password')
        place = Place(name='My Place', description='A nice place', address='123 Street', city_id=1, host_id=host.id, 
                      price_per_night=100, latitude=40.7128, longitude=-74.0060, number_of_rooms=3, number_of_bathrooms=2, max_guests=4)
        place.add_amenity('WiFi')
        self.assertIn('WiFi', place.amenities)

if __name__ == '__main__':
    unittest.main()
