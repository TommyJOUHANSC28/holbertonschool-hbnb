"""
Place entity model.
Includes relationships with User, Review and Amenity.
"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Represents a rental place.
    """

    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if not title:
            raise ValueError("Title is required")

        if price < 0:
            raise ValueError("Price must be positive")

        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")

        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        """
        Adds an amenity to the place.
        """
        self.amenities.append(amenity)

    def add_review(self, review):
        """
        Adds a review to the place.
        """
        self.reviews.append(review)

    def to_dict(self):
        """
        Serializes place with owner and amenities.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner.to_dict(),
            "amenities": [a.to_dict() for a in self.amenities],
            "reviews": [r.to_dict() for r in self.reviews]
        }
