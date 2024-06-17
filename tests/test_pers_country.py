import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ajoutez le répertoire parent à sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from model.country import Country
from persistence.country_repository import CountryRepository

class TestCountryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = CountryRepository()

    def test_get_country(self):
        country = Country(name='France')
        self.repo.save(country)
        fetched_country = self.repo.get(country.country_id)
        self.assertEqual(fetched_country.name, 'France')

    def test_get_all_countries(self):
        country1 = Country(name='France')
        country2 = Country(name='England')
        self.repo.save(country1)
        self.repo.save(country2)
        countries = self.repo.get_all()
        self.assertEqual(len(countries), 2)
        self.assertEqual(countries[0].name, 'France')
        self.assertEqual(countries[1].name, 'England')

    def test_update_country(self):
        country = Country(name='France')
        self.repo.save(country)
        updated_data = {'name': 'Updated France'}
        self.repo.update(country.country_id, updated_data)
        updated_country = self.repo.get(country.country_id)
        self.assertEqual(updated_country.name, 'Updated France')

    def test_delete_country(self):
        country = Country(name='France')
        self.repo.save(country)
        self.assertTrue(self.repo.delete(country.country_id))
        self.assertIsNone(self.repo.get(country.country_id))

    def test_update_nonexistent_country(self):
        self.assertFalse(self.repo.update(999, {'name': 'Nonexistent'}))

    def test_delete_nonexistent_country(self):
        self.assertFalse(self.repo.delete(999))

if __name__ == '__main__':
    unittest.main()