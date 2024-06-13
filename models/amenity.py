import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name, description=""):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def update(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        self.updated_at = datetime.now()
