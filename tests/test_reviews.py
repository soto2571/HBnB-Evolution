import unittest
from app.models import Review, User, Place, City

class TestReview(unittest.TestCase):
    def setUp(self):
        self.user = User(email="reviewer@example.com", password="password", first_name="Reviewer", last_name="User")
        self.city = City(name="Test City", country="Test Country")
        self.place = Place(name="Test Place", description="A place for testing", address="123 Test St", city=self.city, host=self.user, number_of_rooms=2, bathrooms=1, price_per_night=100, max_guests=4)
        self.review = Review(user_id=self.user.id, place_id=self.place.id, rating=5, comment="Great place!")

    def test_create_review(self):
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.user_id, self.user.id)
        self.assertEqual(self.review.place_id, self.place.id)
        self.assertEqual(self.review.rating, 5)

if __name__ == '__main__':
    unittest.main()
