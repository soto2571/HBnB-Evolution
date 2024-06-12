from .base_model import BaseModel
# This file was empty, I added some code based on others files (XCS)

class Amenity(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country  # This should be a Country object
