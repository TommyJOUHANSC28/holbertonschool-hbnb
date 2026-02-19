"""
Review model module
"""
from app.models.baseEntity import BaseEntity, type_validation, strlen_validation
from app.models.place import Place
from app.models.user import User


class Review(BaseEntity):
    """
    Review class represents a review for a place in the HBNB application
    Inherits from BaseEntity for common attributes (id, created_at, updated_at)
    """
    
    def __init__(self, text: str, rating: int, place: Place, user: User):
        """
        Initialize a Review instance
        
        Args:
            text (str): Review text/comment (required, 2-500 chars)
            rating (int): Rating score (1-5, required)
            place (Place): Place object being reviewed (required)
            user (User): User object who wrote the review (required)
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place  # Utilise le setter
        self.user = user    # Utilise le setter
        
        # Add review to place (after validation is complete)
        place.add_review(self)

    # ==================== Text ====================
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        if text is None:
            raise ValueError("Text is required")
        type_validation(text, "text", str)
        text = text.strip()
        strlen_validation(text, "text", 2, 500)
        self.__text = text

    # ==================== Rating ====================
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int) -> None:
        if rating is None:
            raise ValueError("Rating is required")
        type_validation(rating, "rating", int)
        self._validate_rating(rating)
        self.__rating = rating

    def _validate_rating(self, rating: int) -> None:
        """Validate rating is between 1 and 5."""
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")

    # ==================== Place ====================
    @property
    def place(self) -> Place:
        return self.__place

    @place.setter
    def place(self, place: Place) -> None:
        if place is None:
            raise ValueError("Place is required")
        type_validation(place, "place", Place)
        self.__place = place

    # ==================== User ====================
    @property
    def user(self) -> User:
        return self.__user

    @user.setter
    def user(self, user: User) -> None:
        if user is None:
            raise ValueError("User is required")
        type_validation(user, "user", User)
        self.__user = user

    # ==================== Utility ====================
    def __repr__(self) -> str:
        return f"Review(text={self.text[:20]!r}..., rating={self.rating})"

    def to_dict(self) -> dict:
        """Convert Review to dictionary."""
        data = super().to_dict()
        data.update({
            "text": self.text,
            "rating": self.rating,
            "place_id": self.place.id if self.place else None,
            "user_id": self.user.id if self.user else None
        })
        return data
