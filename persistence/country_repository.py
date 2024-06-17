#!/usr/bin/python3
""" Persistence for countries"""

from model.country import Country
from persistence.ipersistence_manager import IPersistenceManager


class CountryRepository(IPersistenceManager):
    """Class for managing the persistence of countries."""

    def __init__(self):
        """Initializes the CountryRepository with an empty
        dictionary and a next_id counter.
        """
        self.countries = {}
        self.next_id = 1

    def save(self, country):
        """
        Saves a country.

        If the country does not have a country_id, it assigns a new unique ID.
        The country is then stored in the countries dictionary.
        """
        if not hasattr(country, 'country_id'):
            country.country_id = self.next_id
            self.next_id += 1
        self.countries[country.country_id] = country

    def get(self, country_id):
        """
        Fetches a country by its ID.

        Args:
            country_id (int): The unique identifier of the country.

        Returns:
            Country: The country object if found, otherwise None.
        """
        return self.countries.get(country_id)

    def get_all(self):
        """
        Fetches all countries.

        Returns:
            list: A list of all country objects.
        """
        return list(self.countries.values())

    def update(self, country_id, new_country_data):
        """
        Updates an existing country.

        Args:
            country_id (int): The unique identifier of
            the country to be updated.
            new_country_data (dict): A dictionary containing
            the new data for the country.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if country_id in self.countries:
            country = self.countries[country_id]
            for key, value in new_country_data.items():
                setattr(country, key, value)
            self.save(country)
            return True
        return False

    def delete(self, country_id):
        """
        Deletes an existing country.

        Args:
            country_id (int): The unique identifier of
            the country to be deleted.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if country_id in self.countries:
            del self.countries[country_id]
            return True
        return False