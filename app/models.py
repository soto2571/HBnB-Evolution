import uuid
from datetime import datetime

users = {}

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class User(BaseModel):
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        if self.email in users:
            raise ValueError("A user with this email already exists.")
        users[self.email] = self

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

class Review(BaseModel):
    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country