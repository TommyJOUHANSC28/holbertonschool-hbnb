#!/usr/bin/python3
from base_model import BaseModel


class Place(BaseModel):
    """Class place"""
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()

        if not title:
            raise ValueError("Title is required")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

        # relations
        self.owner = owner_id
        self.reviews = []
        self.amenities = []

