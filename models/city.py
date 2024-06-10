import uuid
from datetime import datetime

class City:
    def __init__(self, name, country_id):
        self.id = uuid.uuid4()
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
