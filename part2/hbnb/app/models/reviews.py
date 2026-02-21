"""
Review entity model.
"""

from hbnb.app.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place.
    """

    def __init__(self, text, rating, user, place):
        super().__init__()

        if not text or not text.strip():
            raise ValueError("Review text cannot be empty")

        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        self.text = text
        self.rating = rating
        self.user = user
        self.place = place

    def to_dict(self):
        """
        Serializes review.
        """
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user.id,
            "place_id": self.place.id
        }
