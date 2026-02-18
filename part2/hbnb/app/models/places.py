#!/usr/bin/python3

"""Class place"""
from part2.hbnb.app.models.base_model import BaseModel


class Place(BaseModel):

    def __init__(self, id, title, description, price, latitude, longitude):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.longitude = longitude

        self.owner = owner
        self.amenities = []
        self.reviews = []

        owner.place.append(self)

    def create(self):
        print(f"Place {self.id} created")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def delete(self):
        print(f"Place {self.id} deleted")

    def get_review(self):
        return self.reviews
