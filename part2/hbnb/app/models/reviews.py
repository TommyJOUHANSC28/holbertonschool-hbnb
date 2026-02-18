#!/usr/bin/python3

from base_model import BaseModel


class Review(BaseModel):

    def __init__(self, comment, rating, author, place):
        super().__init__()
        self.comment = comment
        self.rating = rating

        # relations
        self.author = author   # User (1)
        self.place = place     # Place (1)

        author.reviews.append(self)
        place.reviews.append(self)

    def create(self):
        print("Review created")

    def read(self):
        return self.comment

    def update(self, comment=None, rating=None):
        if comment:
            self.comment = comment
        if rating:
            self.rating = rating
        self.save()

    def delete(self):
        print("Review deleted")
