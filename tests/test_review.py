import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_create_review(self):
        review = Review(place_id=1, user_id=1, text="Great place!", rating=5)
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.rating, 5)
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

if __name__ == '__main__':
    unittest.main()
