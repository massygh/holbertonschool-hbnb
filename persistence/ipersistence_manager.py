#!/usr/bin/python3
# Persistence Interface

from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """Interface for defining persistence manager methods."""

    @abstractmethod
    def save(self, entity):
        """
        Saves an entity.

        Args:
            entity (object): The entity to be saved.
        """
        pass

    @abstractmethod
    def get(self, entity_id):
        """
        Fetches an entity by its ID.

        Args:
            entity_id (str/int): The unique identifier of the entity.

        Returns:
            object: The entity object if found, otherwise None.
        """
        pass

    @abstractmethod
    def update(self, entity_id, new_data):
        """
        Updates an existing entity.

        Args:
            entity_id (str/int): The unique identifier of
            the entity to be updated.
            new_data (dict): A dictionary containing
            the new data for the entity.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        pass

    @abstractmethod
    def delete(self, entity_id):
        """
        Deletes an existing entity.

        Args:
            entity_id (str/int): The unique identifier
            of the entity to be deleted.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        pass

    @abstractmethod
    def get_all(self):
        """
        Fetches all entities.

        Returns:
            list: A list of all entity objects.
        """
        pass