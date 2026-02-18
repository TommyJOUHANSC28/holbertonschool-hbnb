#!/bin/user/python3

from .base_model import BaseModel


class User(BaseModel):
    """Class Place"""
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

        # relations
        self.places = []      # owns (0..*)
        self.reviews = []     # writes (0..*)

    def register(self):
        print(f"User {self.email} registered")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def delete(self):
        print(f"User {self.email} deleted")

    def validate(self):
        return "@" in self.email
