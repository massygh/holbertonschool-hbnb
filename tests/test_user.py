import unittest
from model.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User(user_id=1, email='test@example.com', name='Test User')
        self.assertEqual(user.email, 'test@example.com')

    def test_unique_email(self):
        user1 = User(user_id=1, email='test@example.com', name='Test User')
        with self.assertRaises(ValueError):
            user2 = User(user_id=2, email='test@example.com', name='Another User')

if __name__ == '__main__':
    unittest.main()
