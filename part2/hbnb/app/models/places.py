#!/usr/bin/python3

"""Class place"""
from part2.hbnb.app.models.base_model import BaseModel


class Place(BaseModel):

    def __init__(self, id, title, description, price, latitude, longitude):
        super().__init__()
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.longitude = longitude
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        self.reviews.append(review)

