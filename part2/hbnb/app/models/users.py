#!/usr/bin/python3

"""Class users"""
from part2.hbnb.app.models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, id, email, password, first_name, last_name, is_admin):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = True if is_admin is True else False

    def register(self):
        print(f"User {self.email} registered")

    def update(self, **kwargs):
        print(f"User {self.email} updated")

    def delete(self):
        print(f"User {self.email} deleted")

    def validate(self):
        return "@" in self.email
