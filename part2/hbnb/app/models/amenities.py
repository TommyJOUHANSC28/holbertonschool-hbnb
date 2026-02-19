#!/usr/bin/python3


from base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity"""
    def __init__(self, name, description=None):
        super().__init__()
        if not name:
            raise ValueError("Amenity name is required")
        self.name = name
        self.description = description

