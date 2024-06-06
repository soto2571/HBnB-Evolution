from .base_model import BaseModel
from .user import User
from .city import City

class Place(BaseModel):
    def __init__(self, name, description, address, city, host, number_of_rooms, bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.host = host
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guest = max_guests
        self.amenities = []
