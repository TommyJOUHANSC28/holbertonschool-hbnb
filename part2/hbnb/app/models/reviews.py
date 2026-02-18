#!/usr/bin/python3

"""Class reviews"""
from part2.hbnb.app.models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, id, comment, rating):
        super().__init__()
        self.id = id
        self.comment = comment
        self.rating = rating
