import unittest
from models.user import User
from models.place import Place
from persistence.DataManager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_save_user(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe", password="password")
        saved_user = self.data_manager.save(user)
        self.assertIsNotNone(saved_user.id)
        self.assertEqual(saved_user.email, "test@example.com")

    def test_get_user(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe", password="password")
        saved_user = self.data_manager.save(user)
        fetched_user = self.data_manager.get(saved_user.id, "User")
        self.assertEqual(fetched_user.email, "test@example.com")

    def test_update_user(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe", password="password")
        saved_user = self.data_manager.save(user)
        saved_user.first_name = "Jane"
        updated_user = self.data_manager.update(saved_user)
        self.assertEqual(updated_user.first_name, "Jane")

    def test_delete_user(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe", password="password")
        saved_user = self.data_manager.save(user)
        result = self.data_manager.delete(saved_user.id, "User")
        self.assertTrue(result)
        self.assertIsNone(self.data_manager.get(saved_user.id, "User"))

if __name__ == '__main__':
    unittest.main()
