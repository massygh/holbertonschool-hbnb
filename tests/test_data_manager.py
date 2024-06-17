from unittest.mock import patch, MagicMock
import unittest
import sys
import os

# Assurez-vous que le répertoire parent est dans le chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.amenity import Amenity
from model.city import City
from model.country import Country
from model.place import Place
from model.review import Review
from model.user import User
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    # Tests for Amenity
    @patch.object(DataManager, 'save_amenity')
    def test_save_amenity(self, mock_save_amenity):
        mock_save_amenity.return_value = 1
        amenity_data = {'name': 'Pool'}
        amenity_id = self.data_manager.save_amenity(amenity_data)
        self.assertEqual(amenity_id, 1)
        mock_save_amenity.assert_called_once_with(amenity_data)

    @patch.object(DataManager, 'get_amenity')
    def test_get_amenity(self, mock_get_amenity):
        mock_amenity = Amenity(name='WiFi')
        mock_get_amenity.return_value = mock_amenity
        result = self.data_manager.get_amenity(1)
        self.assertEqual(result.name, 'WiFi')
        mock_get_amenity.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_amenities')
    def test_get_all_amenities(self, mock_get_all_amenities):
        mock_amenities = [Amenity(name='Pool'), Amenity(name='WiFi')]
        mock_get_all_amenities.return_value = mock_amenities
        result = self.data_manager.get_all_amenities()
        self.assertEqual(len(result), 2)
        mock_get_all_amenities.assert_called_once()

    @patch.object(DataManager, 'update_amenity')
    def test_update_amenity(self, mock_update_amenity):
        mock_update_amenity.return_value = True
        updated_data = {'name': 'Updated Pool'}
        result = self.data_manager.update_amenity(1, updated_data)
        self.assertTrue(result)
        mock_update_amenity.assert_called_once_with(1, updated_data)

    @patch.object(DataManager, 'delete_amenity')
    def test_delete_amenity(self, mock_delete_amenity):
        mock_delete_amenity.return_value = True
        result = self.data_manager.delete_amenity(1)
        self.assertTrue(result)
        mock_delete_amenity.assert_called_once_with(1)

    # Tests for City
    @patch.object(DataManager, 'save_city')
    def test_save_city(self, mock_save_city):
        mock_save_city.return_value = 1
        city_data = {'name': 'Paris', 'country_id': 1}
        city_id = self.data_manager.save_city(city_data)
        self.assertEqual(city_id, 1)
        mock_save_city.assert_called_once_with(city_data)

    @patch.object(DataManager, 'get_city')
    def test_get_city(self, mock_get_city):
        mock_city = City(name='Paris', country_id=1)
        mock_get_city.return_value = mock_city
        result = self.data_manager.get_city(1)
        self.assertEqual(result.name, 'Paris')
        mock_get_city.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_cities')
    def test_get_all_cities(self, mock_get_all_cities):
        mock_cities = [City(name='Paris', country_id=1), City(name='London', country_id=2)]
        mock_get_all_cities.return_value = mock_cities
        result = self.data_manager.get_all_cities()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, 'Paris')
        self.assertEqual(result[1].name, 'London')
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

    # Tests for Country
    @patch.object(DataManager, 'save_country')
    def test_save_country(self, mock_save_country):
        mock_save_country.return_value = 1
        country_data = {'name': 'France'}
        country_id = self.data_manager.save_country(country_data)
        self.assertEqual(country_id, 1)
        mock_save_country.assert_called_once_with(country_data)

    @patch.object(DataManager, 'get_country')
    def test_get_country(self, mock_get_country):
        mock_country = Country(name='France')
        mock_get_country.return_value = mock_country
        result = self.data_manager.get_country(1)
        self.assertEqual(result.name, 'France')
        mock_get_country.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_countries')
    def test_get_all_countries(self, mock_get_all_countries):
        mock_countries = [Country(name='France'), Country(name='England')]
        mock_get_all_countries.return_value = mock_countries
        result = self.data_manager.get_all_countries()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, 'France')
        self.assertEqual(result[1].name, 'England')
        mock_get_all_countries.assert_called_once()

    @patch.object(DataManager, 'update_country')
    def test_update_country(self, mock_update_country):
        mock_update_country.return_value = True
        updated_data = {'name': 'New France'}
        result = self.data_manager.update_country(1, updated_data)
        self.assertTrue(result)
        mock_update_country.assert_called_once_with(1, updated_data)

    @patch.object(DataManager, 'delete_country')
    def test_delete_country(self, mock_delete_country):
        mock_delete_country.return_value = True
        result = self.data_manager.delete_country(1)
        self.assertTrue(result)
        mock_delete_country.assert_called_once_with(1)

    # Tests for Place
    @patch.object(DataManager, 'save_place')
    def test_save_place(self, mock_save_place):
        mock_save_place.return_value = 1
        place_data = {'name': 'Eiffel Tower'}
        place_id = self.data_manager.save_place(place_data)
        self.assertEqual(place_id, 1)
        mock_save_place.assert_called_once_with(place_data)

    @patch.object(DataManager, 'get_place')
    def test_get_place(self, mock_get_place):
        mock_place = Place(name='Eiffel Tower')
        mock_get_place.return_value = mock_place
        result = self.data_manager.get_place(1)
        self.assertEqual(result.name, 'Eiffel Tower')
        mock_get_place.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_places')
    def test_get_all_places(self, mock_get_all_places):
        mock_places = [Place(name='Eiffel Tower'), Place(name='Louvre')]
        mock_get_all_places.return_value = mock_places
        result = self.data_manager.get_all_places()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, 'Eiffel Tower')
        self.assertEqual(result[1].name, 'Louvre')
        mock_get_all_places.assert_called_once()

    @patch.object(DataManager, 'update_place')
    def test_update_place(self, mock_update_place):
        mock_update_place.return_value = True
        updated_data = {'name': 'New Eiffel Tower'}
        result = self.data_manager.update_place(1, updated_data)
        self.assertTrue(result)
        mock_update_place.assert_called_once_with(1, updated_data)

    @patch.object(DataManager, 'delete_place')
    def test_delete_place(self, mock_delete_place):
        mock_delete_place.return_value = True
        result = self.data_manager.delete_place(1)
        self.assertTrue(result)
        mock_delete_place.assert_called_once_with(1)

    # Tests for Review
    @patch.object(DataManager, 'save_review')
    def test_save_review(self, mock_save_review):
        mock_save_review.return_value = 1
        review_data = {'comment': 'Great place!'}
        review_id = self.data_manager.save_review(review_data)
        self.assertEqual(review_id, 1)
        mock_save_review.assert_called_once_with(review_data)

    @patch.object(DataManager, 'get_review')
    def test_get_review(self, mock_get_review):
        mock_review = Review(comment='Great place!')
        mock_get_review.return_value = mock_review
        result = self.data_manager.get_review(1)
        self.assertEqual(result.comment, 'Great place!')
        mock_get_review.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_reviews')
    def test_get_all_reviews(self, mock_get_all_reviews):
        mock_reviews = [Review(comment='Great place!'), Review(comment='Awesome experience!')]
       
