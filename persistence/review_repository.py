#!/usr/bin/python3
# Persistence for reviews

from model.review import Review
from persistence.ipersistence_manager import IPersistenceManager


class ReviewRepository(IPersistenceManager):
    """Class for managing the persistence of reviews."""

    def __init__(self):
        """Initializes the ReviewRepository with an empty
        dictionary and a next_id counter.
        """
        self.reviews = {}
        self.next_id = 1

    def save(self, review):
        """
        Saves a review.

        If the review does not have a review_id, it assigns a new unique ID.
        The review is then stored in the reviews dictionary.
        """
        if not hasattr(review, 'review_id'):
            review.review_id = self.next_id
            self.next_id += 1
        self.reviews[review.review_id] = review

    def get(self, review_id):
        """
        Fetches a review by its ID.

        Args:
            review_id (int): The unique identifier of the review.

        Returns:
            Review: The review object if found, otherwise None.
        """
        return self.reviews.get(review_id)

    def get_all(self):
        """
        Fetches all reviews.

        Returns:
            list: A list of all review objects.
        """
        return list(self.reviews.values())

    def update(self, review_id, new_review_data):
        """
        Updates an existing review.

        Args:
            review_id (int): The unique identifier
            of the review to be updated.
            new_review_data (dict): A dictionary containing
            the new data for the review.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if review_id in self.reviews:
            review = self.reviews[review_id]
            for key, value in new_review_data.items():
                setattr(review, key, value)
            self.save(review)
            return True
        return False

    def delete(self, review_id):
        """
        Deletes an existing review.

        Args:
            review_id (int): The unique identifier of the review to be deleted.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False