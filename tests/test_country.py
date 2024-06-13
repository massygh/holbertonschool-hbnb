import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def test_create_country(self):
        country = Country(code="US", name="United States")
        self.assertEqual(country.code, "US")
        self.assertEqual(country.name, "United States")

if __name__ == '__main__':
    unittest.main()
