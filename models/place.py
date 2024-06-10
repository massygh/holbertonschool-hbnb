from datetime import datetime

class Place:
    def __init__(self, place_id, host, name, location):
        self.place_id = place_id
        self.host = host  # Cela devrait être un objet User
        self.name = name
        self.location = location
        self.amenities = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.updated_at = datetime.now()