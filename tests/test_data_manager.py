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
        self.city = City(name="Test City", country="Test Country")
        self.place = Place(name="Test Place", description="A place for testing", address="123 Test St", city=self.city, host=self.user, number_of_rooms=2, bathrooms=1, price_per_night=100, max_guests=4)
        self.review = Review(user_id=self.user.id, place_id=self.place.id, rating=5, comment="Great place!")

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

    def test_save_place(self):
        self.data_manager.save(self.place)
        retrieved_place = self.data_manager.get(self.place.id, 'Place')
        self.assertEqual(retrieved_place.name, "Test Place")

    def test_update_place(self):
        self.data_manager.save(self.place)
        self.place.name = "Updated Place Name"
        self.data_manager.update(self.place)
        retrieved_place = self.data_manager.get(self.place.id, 'Place')
        self.assertEqual(retrieved_place.name, "Updated Place Name")

    def test_delete_place(self):
        self.data_manager.save(self.place)
        self.data_manager.delete(self.place.id, 'Place')
        retrieved_place = self.data_manager.get(self.place.id, 'Place')
        self.assertIsNone(retrieved_place)

    def test_save_review(self):
        self.data_manager.save(self.review)
        retrieved_review = self.data_manager.get(self.review.id, 'Review')
        self.assertEqual(retrieved_review.rating, 5)

    def test_update_review(self):
        self.data_manager.save(self.review)
        self.review.rating = 4
        self.data_manager.update(self.review)
        retrieved_review = self.data_manager.get(self.review.id, 'Review')
        self.assertEqual(retrieved_review.rating, 4)

    def test_delete_review(self):
        self.data_manager.save(self.review)
        self.data_manager.delete(self.review.id, 'Review')
        retrieved_review = self.data_manager.get(self.review.id, 'Review')
        self.assertIsNone(retrieved_review)

    def test_save_city(self):
        self.data_manager.save(self.city)
        retrieved_city = self.data_manager.get(self.city.id, 'City')
        self.assertEqual(retrieved_city.name, "Test City")

    def test_update_city(self):
        self.data_manager.save(self.city)
        self.city.name = "Updated City Name"
        self.data_manager.update(self.city)
        retrieved_city = self.data_manager.get(self.city.id, 'City')
        self.assertEqual(retrieved_city.name, "Updated City Name")

    def test_delete_city(self):
        self.data_manager.save(self.city)
        self.data_manager.delete(self.city.id, 'City')
        retrieved_city = self.data_manager.get(self.city.id, 'City')
        self.assertIsNone(retrieved_city)

if __name__ == '__main__':
    unittest.main()
