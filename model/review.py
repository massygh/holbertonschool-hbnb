#!/usr/bin/python3
"""Model for representing reviews."""

import uuid
from datetime import datetime


class Review:
    """Class representing a review."""

    def __init__(self, user_id, place_id, rating, comment):
        # Generate a UUID4 for unique identification
        self.review_id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()  # Record creation timestamp
        self.updated_at = datetime.now()  # Record update timestamp

    def to_dict(self):
        """Returns the review data as a dictionary."""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment,
            # Convert datetime to ISO 8601 format
            'created_at': self.created_at.isoformat(),
            # Convert datetime to ISO 8601 format
            'updated_at': self.updated_at.isoformat()
        }