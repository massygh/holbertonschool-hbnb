from persistence.IPersistenceManager import IPersistenceManager
from models.user import User
from models.city import City
from models.country import Country
from models.amenity import Amenity
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
        self.preload_countries()

    def preload_countries(self):
        countries = [
            {"code": "US", "name": "United States"},
            {"code": "CA", "name": "Canada"},
            {"code": "FR", "name": "France"},
            # Add more countries as needed
        ]
        for country in countries:
            self.storage['Country'][country['code']] = Country(country['code'], country['name'])

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type == 'User' and not User.is_email_unique(entity.email, self.storage['User'].values()):
            return False  # email is not unique

        if isinstance(entity, City) and not self.get(entity.country_code, 'Country'):
            return False  # invalid country code

        if isinstance(entity, Amenity):
            for amenity in self.storage['Amenity'].values():
                if amenity.name == entity.name:
                    return False  # duplicate amenity name

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
