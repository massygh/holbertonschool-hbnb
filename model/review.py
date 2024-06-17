#!/usr/bin/python3
"""Model for representing reviews."""

import uuid
from datetime import datetime


class Review:
    """Class representing a review."""

    def __init__(self, user_id, place_id, rating, comment, review_id=None, created_at=None, updated_at=None):
        # Generate a UUID4 for unique identification
        self.review_id = review_id if review_id is not None else str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at if updated_at is not None else datetime.now()

    def to_dict(self):
        """Returns the review data as a dictionary."""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
