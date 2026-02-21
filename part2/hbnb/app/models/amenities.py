"""
Amenity entity model.
"""

from hbnb.app.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity for places.
    """

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.places = []
