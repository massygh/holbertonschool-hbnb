import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, address, city_id, host_id, price_per_night, latitude, longitude, number_of_rooms, number_of_bathrooms, max_guests):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.host_id = host_id
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'host_id': self.host_id,
            'price_per_night': self.price_per_night,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'max_guests': self.max_guests,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'amenities': self.amenities
        }
