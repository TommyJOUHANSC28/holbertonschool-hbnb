"""
User entity model.
Handles validation and serialization.
"""

import re
from hbnb.app.base_model import BaseModel


class User(BaseModel):
    """
    Represents a system user.
    """

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if not first_name:
            raise ValueError("First name is required")

        if not last_name:
            raise ValueError("Last name is required")

        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            raise ValueError("Invalid email format")

        def __init__(self, email, first_name, last_name, password, user_id, is_admin=False):
            super().__init__()
            self.email = email
            self.first_name = first_name
            self.last_name = last_name
            self.password = password
            self.is_admin = is_admin
            self.user_id = user_id

            self.places = []
            self.reviews = []

    def to_dict(self):
        """
        Serializes user object.
        Password excluded intentionally.
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
