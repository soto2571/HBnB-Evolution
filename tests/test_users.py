import unittest
from app.models.user import User, clear_users

class TestUser(unittest.TestCase):
    def setUp(self):
        clear_users()
        self.user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")

    def test_create_user(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_unique_email(self):
        self.user.save()
        user2 = User(email="test@example.com", password="password123", first_name="Jane", last_name="Doe")
        with self.assertRaises(ValueError):
            user2.save()

if __name__ == '__main__':
    unittest.main()

