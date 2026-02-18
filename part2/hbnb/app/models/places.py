#!/usr/bin/python3
from base_model import BaseModel


class Place(BaseModel):
    """Class place"""
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

        # relations
        self.owner = owner        # User (1)
        self.reviews = []         # has (0..*)
        self.amenities = []       # includes (0..*)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
