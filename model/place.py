#!/usr/bin/python3
"""Model for representing places."""

import uuid
from datetime import datetime

class Place:
    """Class representing a place."""

    def __init__(
        self, name, description, address, city_id, latitude, longitude,
        host_id, number_of_rooms, number_of_bathrooms, price_per_night,
        max_guests, amenity_ids, place_id=None, created_at=None, updated_at=None
    ):
        self.place_id = place_id if place_id is not None else str(uuid.uuid4())
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenity_ids = amenity_ids
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at if updated_at is not None else datetime.now()
        self.reviews = []

    def add_review(self, review):
        """Adds a review."""
        self.reviews.append(review)

    def calculate_total_price(self, number_of_nights):
        """Calculates the total price for a number of nights."""
        return self.price_per_night * number_of_nights

    def list_amenities(self):
        """Lists the amenities."""
        return self.amenity_ids

    def check_availability(self, start_date, end_date):
        """Checks availability."""
        pass

    def list_reviews(self):
        """Lists the reviews."""
        return self.reviews

    def set_number_of_guests(self, number):
        """Sets the number of guests."""
        self.max_guests = number

    def add_description(self, description):
        """Adds a description."""
        self.description = description

    def set_number_of_rooms(self, number):
        """Sets the number of rooms."""
        self.number_of_rooms = number

    def set_location(self, latitude, longitude):
        """Sets the location."""
        self.latitude = latitude
        self.longitude = longitude

    def add_amenity(self, amenity_id):
        """Adds an amenity."""
        self.amenity_ids.append(amenity_id)

    def toggle_availability(self):
        """Toggles availability."""
        pass

    def get_description(self):
        """Gets the description."""
        return self.description

    def get_location(self):
        """Gets the location."""
        return self.latitude, self.longitude

    def update_place_data(self, new_data):
        """Updates the place data with new data."""
        for key, value in new_data.items():
            setattr(self, key, value)

    def delete_amenity(self, amenity_id):
        """Deletes an amenity from the place by its ID."""
        if amenity_id in self.amenity_ids:
            self.amenity_ids.remove(amenity_id)

    def to_dict(self):
        """Returns the place data as a dictionary."""
        return {
            'place_id': self.place_id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenity_ids': self.amenity_ids,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'reviews': self.reviews
        }
