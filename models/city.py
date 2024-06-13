import uuid
from datetime import datetime

class City:
    def __init__(self, name, country_code):
        self.id = uuid.uuid4()
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'country_code': self.country_code,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    def update(self, name=None, country_code=None):
        if name:
            self.name = name
        if country_code:
            self.country_code = country_code
        self.updated_at = datetime.now()
