import unittest
from app.models.user import User, clear_users
from app.models.place import Place
from app.models.city import City
from app.models.review import Review
from app.persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        clear_users()
        self.user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")

    def test_save_user(self):
        self.data_manager.save(self.user)
        retrieved_user = self.data_manager.get(self.user.id, 'User')
        self.assertEqual(retrieved_user.email, "test@example.com")

    def test_get_non_existent_user(self):
        retrieved_user = self.data_manager.get("non-existent-id", 'User')
        self.assertIsNone(retrieved_user)

    def test_update_user(self):
        self.data_manager.save(self.user)
        self.user.first_name = "Jane"
        self.data_manager.update(self.user)
        retrieved_user = self.data_manager.get(self.user.id, 'User')
        self.assertEqual(retrieved_user.first_name, "Jane")

    def test_delete_user(self):
        self.data_manager.save(self.user)
        self.data_manager.delete(self.user.id, 'User')
        retrieved_user = self.data_manager.get(self.user.id, 'User')
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()
