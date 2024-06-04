import unittest
from app.models import Place, User, City

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.user = User(email="host@example.com", password="password", first_name="Host", last_name="User")
        self.city = City(name="Test City", country="Test Country")
        self.place = Place(name="Test Place", description="A place for testing", address="123 Test St", city=self.city, host=self.user, number_of_rooms=2, bathrooms=1, price_per_night=100, max_guests=4)


    def test_create_place(self):
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.host, self.user)
        self.assertEqual(self.place.city, self.city)

    def test_add_amenities(self):
        self.place.amenities.append("Wi-Fi")
        self.place.amenities.append("Pool")
        self.assertIn("Wi-Fi", self.place.amenities)
        self.assertIn("Pool", self.place.amenities)

if __name__ == '__main__':
    unittest.main()