#!/usr/bin/python3
import unittest
from model.user import User
from persistence.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.user_repository = UserRepository()

    def test_save_get(self):
        user = User(name="John", email="john@example.com")
        self.user_repository.save(user)
        retrieved_user = self.user_repository.get(user.user_id)
        self.assertEqual(user, retrieved_user)

    def test_get_all(self):
        users = [
            User(name="John", email="john@example.com"),
            User(name="Jane", email="jane@example.com"),
            User(name="Doe", email="doe@example.com")
        ]
        for user in users:
            self.user_repository.save(user)
        retrieved_users = self.user_repository.get_all()
        self.assertEqual(len(retrieved_users), len(users))

    def test_update(self):
        user = User(name="John", email="john@example.com")
        self.user_repository.save(user)
        updated_data = {"name": "Johnny", "email": "johnny@example.com"}
        self.user_repository.update(user.user_id, updated_data)
        updated_user = self.user_repository.get(user.user_id)
        self.assertEqual(updated_user.name, updated_data["name"])
        self.assertEqual(updated_user.email, updated_data["email"])

    def test_delete(self):
        user = User(name="John", email="john@example.com")
        self.user_repository.save(user)
        self.assertTrue(self.user_repository.delete(user.user_id))
        self.assertIsNone(self.user_repository.get(user.user_id))


if __name__ == '__main__':
    unittest.main()