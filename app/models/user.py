from .base_model import BaseModel

users = {}

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

def clear_users():
    users.clear()

