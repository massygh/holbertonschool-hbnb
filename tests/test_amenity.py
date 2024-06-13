import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_create_amenity(self):
        amenity = Amenity(name="Wi-Fi", description="High-speed internet")
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertEqual(amenity.description, "High-speed internet")

if __name__ == '__main__':
    unittest.main()
