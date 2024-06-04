import unittest
from app.models import User, users

class TestUser(unittest.TestCase):
    def setUp(self):
        users.clear()
        self.user = User(email="unique@example.com", password="password", first_name="John", last_name="Doe")
        self.user.save()

    def test_create_user(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "unique@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


    def test_unique_email(self):
         user2 = User(email="unique@example.com", password="password123", first_name="Jane", last_name="Doe")
         with self.assertRaises(ValueError):
            user2.save()  # Assuming save method checks for unique email and raises ValueError

if __name__ == '__main__':
    unittest.main()
