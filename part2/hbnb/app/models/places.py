"""
Place model module
"""
from app.models.baseEntity import BaseEntity, type_validation, strlen_validation
from app.models.user import User


class Place(BaseEntity):
    """
    Place class represents a property/accommodation in the HBNB application
    Inherits from BaseEntity for common attributes (id, created_at, updated_at)
    """
    
    def __init__(self, title: str, description: str = None, price: float = None,
                 latitude: float = None, longitude: float = None, owner: User = None):
        """
        Initialize a Place instance
        
        Args:
            title (str): Title of the place (required)
            description (str): Detailed description (optional)
            price (float): Price per night, must be positive (optional)
            latitude (float): Latitude coordinate between -90 and 90 (optional)
            longitude (float): Longitude coordinate between -180 and 180 (optional)
            owner (User): User object who owns this place (required)
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review) -> None:
        """Add a review to the place."""
        from app.models.review import Review
        type_validation(review, "review", Review)
        self.reviews.append(review)

    def add_amenity(self, amenity) -> None:
        """Add an amenity to the place."""
        from app.models.amenity import Amenity
        type_validation(amenity, "amenity", Amenity)
        self.amenities.append(amenity)

    # ==================== Title ====================
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        self.__title = self._validate_title(value)

    def _validate_title(self, title: str) -> str:
        """Validate title: required, string, 1-100 characters."""
        if title is None:
            raise ValueError("Title is required")
        type_validation(title, "title", str)
        title = title.strip()
        strlen_validation(title, "title", 1, 100)
        return title

    # ==================== Description ====================
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description = self._validate_description(value)

    def _validate_description(self, description: str) -> str:
        """Validate description: string, 0-500 characters."""
        if description is None:
            return ""
        type_validation(description, "description", str)
        description = description.strip()
        strlen_validation(description, "description", 0, 500)
        return description

    # ==================== Price ====================
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        self.__price = self._validate_price(value)

    def _validate_price(self, price: float) -> float:
        """Validate price: required, positive number."""
        if price is None:
            raise ValueError("Price is required")
        type_validation(price, "price", (int, float))
        if price <= 0:
            raise ValueError("Price must be a positive number")
        return float(price)

    # ==================== Latitude ====================
    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, value: float) -> None:
        self.__latitude = self._validate_latitude(value)

    def _validate_latitude(self, latitude: float) -> float:
        """Validate latitude: between -90.0 and 90.0."""
        if latitude is None:
            return None
        type_validation(latitude, "latitude", (int, float))
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return float(latitude)

    # ==================== Longitude ====================
    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, value: float) -> None:
        self.__longitude = self._validate_longitude(value)

    def _validate_longitude(self, longitude: float) -> float:
        """Validate longitude: between -180.0 and 180.0."""
        if longitude is None:
            return None
        type_validation(longitude, "longitude", (int, float))
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return float(longitude)

    # ==================== Owner ====================
    @property
    def owner(self) -> User:
        return self.__owner

    @owner.setter
    def owner(self, value: User) -> None:
        if value is None:
            raise ValueError("Owner is required")
        type_validation(value, "owner", User)
        self.__owner = value

    # ==================== Utility methods ====================
    def __repr__(self) -> str:
        return f"Place(title={self.title!r}, price={self.price})"

    def to_dict(self) -> dict:
        """Convert Place to dictionary."""
        data = super().to_dict()
        data.update({
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner.id if self.owner else None,
            "amenities": [a.id for a in self.amenities],
            "reviews": [r.id for r in self.reviews]
        })
        return data
