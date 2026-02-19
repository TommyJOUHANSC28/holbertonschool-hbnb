"""
Amenity entity model.
"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity for places.
    """

    def __init__(self, name):
        super().__init__()

        if not name:
            raise ValueError("Amenity name is required")

        if len(name) > 50:
            raise ValueError("Amenity name must be less than 50 characters")

        self.name = name

    def to_dict(self):
        """
        Serializes amenity.
        """
        return {
            "id": self.id,
            "name": self.name
        }
