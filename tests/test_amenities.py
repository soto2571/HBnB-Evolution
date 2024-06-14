import unittest
from app.models.amenities import Amenity



class TestAmenities(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.amenity1 = Amenity(name="Wi-Fi", country="Test Country")
        self.amenity2 = Amenity(name="Pool", country="Test Country")

    def test_create_amenity(self):
        self.assertIsInstance(self.amenity1, Amenity)
        self.assertEqual(self.amenity1.name, "Wi-Fi")
        self.assertEqual(self.amenity1.country, "Test Country")

    def test_add_amenity_to_list(self):
        amenities_list = []
        amenities_list.append(self.amenity1)
        amenities_list.append(self.amenity2)
        
        self.assertEqual(len(amenities_list), 2)
        self.assertIn(self.amenity1, amenities_list)
        self.assertIn(self.amenity2, amenities_list)

    def test_amenity_attributes(self):
        self.assertEqual(self.amenity1.name, "Wi-Fi")
        self.assertEqual(self.amenity1.country, "Test Country")

if __name__ == '__main__':
    unittest.main()
