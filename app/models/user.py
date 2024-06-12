from app.models.base_model import BaseModel
from app.persistence.data_manager import DataManager

data_manager = DataManager()

class User(BaseModel):
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        for user in data_manager.storage['User'].values():
            if user.email == self.email:
                raise ValueError("A user with this email already exists.")
        data_manager.save(self)

def clear_users():
    data_manager.storage['User'].clear()

