from persistence.IPersistenceManager import IPersistenceManager
from models.user import User
import uuid
from datetime import datetime

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
        if entity_type == 'User' and not User.is_email_unique(entity.email, self.storage['User'].values()):
            return False  # email is not unique

        entity.id = uuid.uuid4()
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.storage[entity_type][entity.id] = entity
        return entity

    def get(self, entity_id, entity_type):
        return self.storage[entity_type].get(entity_id)

    def get_all(self, entity_type):
        return list(self.storage[entity_type].values())

    def update(self, entity):
        entity_type = type(entity).__name__
        entity.updated_at = datetime.now()
        if entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
            return entity
        return None

    def delete(self, entity_id, entity_type):
        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            return True
        return False
