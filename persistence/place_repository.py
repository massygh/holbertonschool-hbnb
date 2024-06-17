#!/usr/bin/python3
"""Persistence for places"""

from model.place import Place
from persistence.ipersistence_manager import IPersistenceManager


class PlaceRepository(IPersistenceManager):
    """Class for managing the persistence of places."""

    def __init__(self):
        """Initializes the PlaceRepository with an empty
        dictionary and a next_id counter.
        """
        self.places = {}
        self.next_id = 1

    def save(self, place):
        """
        Saves a place.

        If the place does not have a place_id, it assigns a new unique ID.
        The place is then stored in the places dictionary.
        """
        if not hasattr(place, 'place_id'):
            place.place_id = self.next_id
            self.next_id += 1
        self.places[place.place_id] = place

    def get(self, place_id):
        """
        Fetches a place by its ID.

        Args:
            place_id (int): The unique identifier of the place.

        Returns:
            Place: The place object if found, otherwise None.
        """
        return self.places.get(place_id)

    def get_all(self):
        """
        Fetches all places.

        Returns:
            list: A list of all place objects.
        """
        return list(self.places.values())

    def update(self, place_id, new_place_data):
        """
        Updates an existing place.

        Args:
            place_id (int): The unique identifier of the place to be updated.
            new_place_data (dict): A dictionary containing
            the new data for the place.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if place_id in self.places:
            place = self.places[place_id]
            place.update_place_data(new_place_data)
            self.save(place)
            return True
        return False

    def delete(self, place_id):
        """
        Deletes an existing place.

        Args:
            place_id (int): The unique identifier of the place to be deleted.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False