#!/usr/bin/python3
"""Model for representing users."""

import uuid
from datetime import datetime


class User:
    """Class representing a user."""
    def __init__(self, username, email, password):
        # Generate a UUID4 for unique identification
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        # In a real-world scenario, hash the password before storing it
        self.password = password
        self.created_at = datetime.now()  # Record creation timestamp
        self.updated_at = datetime.now()  # Record update timestamp
        self.reviews = []

    def add_review(self, review):
        """Adds a review."""
        self.reviews.append(review)

    def list_reviews(self):
        """Lists the reviews."""
        return self.reviews

    def update_user_data(self, new_data):
        """Updates the user data with new data."""
        for key, value in new_data.items():
            setattr(self, key, value)

    def check_password(self, password):
        """Checks if the password is correct."""
        # In a real-world scenario, compare hashed passwords
        return self.password == password

    def to_dict(self):
        """Returns the user data as a dictionary."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            # Convert datetime to ISO 8601 format
            'created_at': self.created_at.isoformat(),
            # Convert datetime to ISO 8601 format
            'updated_at': self.updated_at.isoformat(),
            'reviews': self.reviews
        }