#!/usr/bin/python3

from base_model import BaseModel


class Review(BaseModel):

    def __init__(self, comment, rating, user_id, place_id):
        super().__init__()

        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")

        self.comment = comment
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
