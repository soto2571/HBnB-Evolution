import unittest
from app.models import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")


    def test_create_user(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


    def test_unique_email(self):
         user2 = User(email="test@example.com", password="password123", first_name="Jane", last_name="Doe")
        with self.assertRaises(ValueError):
            user2.save()  # Assuming save method checks for unique email and raises ValueError

if __name__ == '__main__':
    unittest.main()
