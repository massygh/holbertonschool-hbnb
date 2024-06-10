from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        """
        Save an entity to the storage.
        :param entity: The entity to be saved.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve an entity based on its ID and type.
        :param entity_id: The ID of the entity.
        :param entity_type: The type of the entity.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update an entity in the storage.
        :param entity: The entity to be updated.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity from the storage.
        :param entity_id: The ID of the entity.
        :param entity_type: The type of the entity.
        """
        pass
