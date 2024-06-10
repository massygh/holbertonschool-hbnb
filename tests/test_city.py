import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_create_city(self):
        city = City(name="San Francisco", country_id=1)
        self.assertEqual(city.name, "San Francisco")
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.country_id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

if __name__ == '__main__':
    unittest.main()
