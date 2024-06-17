#!/usr/bin/python3

import unittest
from model.review import Review
from persistence.review_repository import ReviewRepository


class TestReviewRepository(unittest.TestCase):

    def setUp(self):
        self.repository = ReviewRepository()

    def test_save_review(self):
        review = Review("John Doe", "Great product!")
        self.repository.save(review)
        self.assertIn(review.review_id, self.repository.reviews)

    def test_save_review_with_existing_id(self):
        review = Review("Alice", "Very detailed review")
        review.review_id = 5
        self.repository.save(review)
        self.assertEqual(self.repository.reviews[5].author, "Alice")

    def test_get_review(self):
        review = Review("Bob", "Nice service")
        self.repository.save(review)
        retrieved_review = self.repository.get(review.review_id)
        self.assertEqual(retrieved_review.author, "Bob")

    def test_get_review_non_existing_id(self):
        retrieved_review = self.repository.get(100)
        self.assertIsNone(retrieved_review)

    def test_get_all_reviews(self):
        review1 = Review("Alice", "Good experience")
        review2 = Review("Charlie", "Could be better")
        self.repository.save(review1)
        self.repository.save(review2)
        all_reviews = self.repository.get_all()
        self.assertEqual(len(all_reviews), 2)

    def test_update_review(self):
        review = Review("Eve", "Fast delivery")
        self.repository.save(review)
        update_data = {"author": "Eve Updated",
                       "content": "Super fast delivery!"}
        self.repository.update(review.review_id, update_data)
        updated_review = self.repository.get(review.review_id)
        self.assertEqual(updated_review.author, "Eve Updated")
        self.assertEqual(updated_review.content, "Super fast delivery!")

    def test_update_non_existing_review(self):
        update_data = {"author": "Nonexistent",
                       "content": "This shouldn't work"}
        result = self.repository.update(100, update_data)
        self.assertFalse(result)

    def test_delete_review(self):
        review = Review("Mallory", "Bad experience, wouldn't recommend")
        self.repository.save(review)
        self.repository.delete(review.review_id)
        deleted_review = self.repository.get(review.review_id)
        self.assertIsNone(deleted_review)

    def test_delete_non_existing_review(self):
        result = self.repository.delete(100)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()