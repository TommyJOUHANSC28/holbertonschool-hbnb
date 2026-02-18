#!/usr/bin/python3


from base_model import BaseModel



class Amenity(BaseModel):
    """Class Amenity"""
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def create(self):
        print(f"Amenity {self.name} created")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def delete(self):
        print(f"Amenity {self.name} deleted")
