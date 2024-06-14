import unittest
from app.models.city import City


class TestCities(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.city1 = City(name="City A", country="Test Country A")
        self.city2 = City(name="City B", country="Test Country B")

    def test_create_city(self):
        self.assertIsInstance(self.city1, City)
        self.assertEqual(self.city1.name, "City A")
        self.assertEqual(self.city1.country, "Test Country A")

    def test_city_attributes(self):
        self.assertEqual(self.city1.name, "City A")
        self.assertEqual(self.city1.country, "Test Country A")

if __name__ == '__main__':
    unittest.main()
