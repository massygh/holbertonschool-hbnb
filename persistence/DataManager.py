import uuid
from datetime import datetime
from .IPersistenceManager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {
            'User': {},
            'Place': {},
            'Review': {},
            'Amenity': {},
            'City': {},
            'Country': {}
        }

    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = uuid.uuid4()
        entity.id = entity_id
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.storage[entity_type][entity_id] = entity
        return entity

    def get(self, entity_id, entity_type):
        return self.storage[entity_type].get(entity_id)

    def update(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.id
        entity.updated_at = datetime.now()
        if entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity
            return entity
        return None

    def delete(self, entity_id, entity_type):
        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            return True
        return False
