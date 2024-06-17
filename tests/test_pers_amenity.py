import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from model.amenity import Amenity
from data_manager import DataManager
# Add le répertoire parent au sys.path for modules puissent être importés
sys.path.insert(0, os.path.abspath(os.path.join
                                   (os.path.dirname(__file__), '..')))


class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    @patch.object(DataManager, 'save_amenity')
    def test_save_amenity(self, mock_save_amenity):
        mock_save_amenity.return_value = '1'
        new_amenity_data = {'name': 'Pool'}
        amenity_id = self.data_manager.save_amenity(new_amenity_data)
        self.assertEqual(amenity_id, '1')
        mock_save_amenity.assert_called_once_with(new_amenity_data)

    @patch.object(DataManager, 'get_amenity')
    def test_get_amenity(self, mock_get_amenity):
        mock_amenity = Amenity(name='WiFi')
        mock_get_amenity.return_value = mock_amenity
        amenity = self.data_manager.get_amenity(1)
        self.assertEqual(amenity.name, 'WiFi')
        mock_get_amenity.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_amenities')
    def test_get_all_amenities(self, mock_get_all_amenities):
        mock_amenities = [
            Amenity(name='Pool'),
            Amenity(name='WiFi')
        ]
        mock_get_all_amenities.return_value = mock_amenities
        amenities = self.data_manager.get_all_amenities()
        self.assertEqual(len(amenities), 2)
        self.assertEqual(amenities[0].name, 'Pool')
        self.assertEqual(amenities[1].name, 'WiFi')
        mock_get_all_amenities.assert_called_once()

    @patch.object(DataManager, 'update_amenity')
    def test_update_amenity(self, mock_update_amenity):
        mock_update_amenity.return_value = True
        updated_data = {'name': 'Updated Gym'}
        result = self.data_manager.update_amenity(1, updated_data)
        self.assertTrue(result)
        mock_update_amenity.assert_called_once_with(1, updated_data)

    @patch.object(DataManager, 'delete_amenity')
    def test_delete_amenity(self, mock_delete_amenity):
        mock_delete_amenity.return_value = True
        result = self.data_manager.delete_amenity(1)
        self.assertTrue(result)
        mock_delete_amenity.assert_called_once_with(1)

    @patch.object(DataManager, 'update_amenity')
    def test_update_nonexistent_amenity(self, mock_update_amenity):
        mock_update_amenity.return_value = False
        result = self.data_manager.update_amenity(999, {'name': 'Nonexistent'})
        self.assertFalse(result)
        mock_update_amenity.assert_called_once_with(999,
                                                    {'name': 'Nonexistent'})

    @patch.object(DataManager, 'delete_amenity')
    def test_delete_nonexistent_amenity(self, mock_delete_amenity):
        mock_delete_amenity.return_value = False
        result = self.data_manager.delete_amenity(999)
        self.assertFalse(result)
        mock_delete_amenity.assert_called_once_with(999)


if __name__ == '__main__':
    unittest.main()