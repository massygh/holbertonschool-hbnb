import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def test_create_country(self):
        country = Country(name="United States")
        self.assertEqual(country.name, "United States")
        self.assertIsNotNone(country.id)

if __name__ == '__main__':
    unittest.main()
