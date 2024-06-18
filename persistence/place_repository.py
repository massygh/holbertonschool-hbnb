#!/usr/bin/python3
"""Repository for managing place data."""

class PlaceRepository:
    """Class to handle place persistence."""

    def __init__(self):
        self.places = {}

    def save(self, place):
        self.places[place.place_id] = place

    def get(self, place_id):
        return self.places.get(place_id)

    def update(self, place_id, place_data):
        if place_id in self.places:
            self.places[place_id].update_place_data(place_data)
            return True
        return False

    def delete(self, place_id):
        return self.places.pop(place_id, None) is not None

    def get_all(self):
        return list(self.places.values())
