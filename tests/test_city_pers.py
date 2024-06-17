import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Assurez-vous que le répertoire parent est dans le chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.city import City
from data_manager import DataManager

class TestCityRepository(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    @patch.object(DataManager, 'save_city')
    def test_save_city(self, mock_save_city):
        mock_save_city.return_value = 1
        new_city_data = {'name': 'Paris', 'country_id': 1}
        city_id = self.data_manager.save_city(new_city_data)
        self.assertEqual(city_id, 1)
        mock_save_city.assert_called_once_with(new_city_data)

    @patch.object(DataManager, 'get_city')
    def test_get_city(self, mock_get_city):
        mock_city = City(name='Paris', country_id=1)
        mock_get_city.return_value = mock_city
        city = self.data_manager.get_city(1)
        self.assertEqual(city.name, 'Paris')
        mock_get_city.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_cities')
    def test_get_all_cities(self, mock_get_all_cities):
        mock_cities = [City(name='Paris', country_id=1), City(name='London', country_id=2)]
        mock_get_all_cities.return_value = mock_cities
        cities = self.data_manager.get_all_cities()
        self.assertEqual(len(cities), 2)
        self.assertEqual(cities[0].name, 'Paris')
        self.assertEqual(cities[1].name, 'London')
        mock_get_all_cities.assert_called_once()

    @patch.object(DataManager, 'update_city')
    def test_update_city(self, mock_update_city):
        mock_update_city.return_value = True
        updated_data = {'name': 'New Paris'}
        result = self.data_manager.update_city(1, updated_data)
        self.assertTrue(result)
        mock_update_city.assert_called_once_with(1, updated_data)

    @patch.object(DataManager, 'delete_city')
    def test_delete_city(self, mock_delete_city):
        mock_delete_city.return_value = True
        result = self.data_manager.delete_city(1)
        self.assertTrue(result)
        mock_delete_city.assert_called_once_with(1)

    @patch.object(DataManager, 'update_city')
    def test_update_nonexistent_city(self, mock_update_city):
        mock_update_city.return_value = False
        result = self.data_manager.update_city(999, {'name': 'Nonexistent'})
        self.assertFalse(result)
        mock_update_city.assert_called_once_with(999, {'name': 'Nonexistent'})

    @patch.object(DataManager, 'delete_city')
    def test_delete_nonexistent_city(self, mock_delete_city):
        mock_delete_city.return_value = False
        result = self.data_manager.delete_city(999)
        self.assertFalse(result)
        mock_delete_city.assert_called_once_with(999)

if __name__ == '__main__':
    unittest.main()