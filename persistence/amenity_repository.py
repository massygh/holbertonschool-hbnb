#!/usr/bin/python3
# Persistence for amenities

import uuid
from model.amenity import Amenity
from persistence.ipersistence_manager import IPersistenceManager


class AmenityRepository(IPersistenceManager):
    """Class for managing the persistence of amenities."""

    def __init__(self):
        """Initializes the AmenityRepository with an empty
        dictionary to store amenities."""
        self.amenities = {}

    def save(self, amenity):
        """
        Saves an amenity.

        If the amenity does not have an amenity_id,
        a new unique ID is generated.
        The amenity is then stored in the amenities dictionary.
        """
        if not hasattr(amenity, 'amenity_id') or amenity.amenity_id is None:
            amenity.amenity_id = str(uuid.uuid4())
        self.amenities[amenity.amenity_id] = amenity

    def get(self, amenity_id):
        """
        Fetches an amenity by its ID.

        Args:
            amenity_id (str): The unique identifier of the amenity.

        Returns:
            Amenity: The amenity object if found, otherwise None.
        """
        return self.amenities.get(amenity_id)

    def get_all(self):
        """
        Fetches all amenities.

        Returns:
            list: A list of all amenity objects.
        """
        return list(self.amenities.values())

    def update(self, amenity_id, new_amenity_data):
        """
        Updates an existing amenity.

        Args:
            amenity_id (str): The unique identifier of
            the amenity to be updated.
            new_amenity_data (dict): A dictionary containing
            the new data for the amenity.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if amenity_id in self.amenities:
            amenity = self.amenities[amenity_id]
            for key, value in new_amenity_data.items():
                setattr(amenity, key, value)
            self.save(amenity)
            return True
        return False

    def delete(self, amenity_id):
        """
        Deletes an existing amenity.

        Args:
            amenity_id (str): The unique identifier of
            the amenity to be deleted.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if amenity_id in self.amenities:
            del self.amenities[amenity_id]
            return True
        return False