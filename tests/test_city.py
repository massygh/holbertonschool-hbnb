import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_create_city(self):
        city = City(name="San Francisco", country_code="US")
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.country_code, "US")

if __name__ == '__main__':
    unittest.main()
