from .base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country
