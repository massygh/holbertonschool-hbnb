#!/usr/bin/python3
# Persistence for cities

import uuid
from model.city import City
from persistence.ipersistence_manager import IPersistenceManager


class CityRepository(IPersistenceManager):
    """Class for managing the persistence of cities."""

    def __init__(self):
        """Initializes the CityRepository with an empty dictionary
        to store cities.
        """
        self.cities = {}

    def save(self, city):
        """
        Saves a city.

        If the city does not have a city_id, a new unique ID is generated.
        The city is then stored in the cities dictionary.
        """
        if not hasattr(city, 'city_id') or city.city_id is None:
            city.city_id = str(uuid.uuid4())
        self.cities[city.city_id] = city

    def get(self, city_id):
        """
        Fetches a city by its ID.

        Args:
            city_id (str): The unique identifier of the city.

        Returns:
            City: The city object if found, otherwise None.
        """
        return self.cities.get(city_id)

    def get_all(self):
        """
        Fetches all cities.

        Returns:
            list: A list of all city objects.
        """
        return list(self.cities.values())

    def update(self, city_id, new_city_data):
        """
        Updates an existing city.

        Args:
            city_id (str): The unique identifier of the city to be updated.
            new_city_data (dict): A dictionary containing the new
            data for the city.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if city_id in self.cities:
            city = self.cities[city_id]
            for key, value in new_city_data.items():
                setattr(city, key, value)
            self.save(city)
            return True
        return False

    def delete(self, city_id):
        """
        Deletes an existing city.

        Args:
            city_id (str): The unique identifier of the city to be deleted.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if city_id in self.cities:
            del self.cities[city_id]
            return True
        return False