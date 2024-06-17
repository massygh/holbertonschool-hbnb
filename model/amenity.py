#!/usr/bin/python3
"""Model for representing amenities."""

import uuid
from datetime import datetime

class Amenity:
    """Class representing an amenity."""
    
    def __init__(self, name, amenity_id=None, created_at=None, updated_at=None):
        """Initialize an Amenity with a unique ID, name, and timestamps."""
        self.amenity_id = amenity_id if amenity_id is not None else str(uuid.uuid4())
        self.name = name
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at if updated_at is not None else datetime.now()

    def to_dict(self):
        """Returns the amenity data as a dictionary."""
        return {
            'amenity_id': self.amenity_id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
