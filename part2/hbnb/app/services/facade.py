"""
Facade module for business logic layer
Provides a simplified interface to interact with models and persistence
"""
import uuid
from app.persistence.repository import InMemoryRepository
from app.models.place import Place
from app.models.review import Review
from app.models.user import User
from app.models.amenity import Amenity
from app.models.baseEntity import type_validation


def is_valid_uuid4) -> bool:
    """
    Validate(uuid_string: str that a string is a valid UUID4
    
    Args:
        uuid_string (str): The string to validate
    
    Returns:
        bool: True if valid UUID4, False otherwise
    """
    try:
        val = uuid.UUID(uuid_string, version=4)
        return str(val) == uuid_string
    except (ValueError, AttributeError):
        return False


class HBnBFacade:
    """
    Facade class that provides a simplified interface for the business logic.
    Acts as an intermediary between the API layer and the models/persistence layer.
    """
    
    def __init__(self):
        """Initialize the facade with repositories for each model type"""
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ==================== User Services ====================
    
    def create_user(self, user_data: dict) -> User:
        """Create a new user with the provided data."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User:
        """Retrieve a user by their ID."""
        if not is_valid_uuid4(user_id):
            raise ValueError("Invalid user_id format")
        return self.user_repo.get(user_id)

    def get_all_users(self) -> list:
        """Retrieve all users from the repository."""
        return self.user_repo.get_all()

    def get_user_by_email(self, email: str) -> User:
        """Retrieve a user by their email address."""
        users = self.user_repo.get_all()
        for user in users:
            if user.email == email:
                return user
        return None

    def update_user(self, user_id: str, user_data: dict) -> User:
        """Update an existing user's data."""
        user = self.get_user(user_id)
        if not user:
            return None
        
        # Update allowed fields
        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']
        
        self.user_repo.update(user_id, user)
        return user

    # ==================== Amenity Services ====================
    
    def create_amenity(self, amenity_data: dict) -> Amenity:
        """Create a new amenity with the provided data."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id: str) -> Amenity:
        """Retrieve an amenity by its ID."""
        if not is_valid_uuid4(amenity_id):
            raise ValueError("Invalid amenity_id format")
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self) -> list:
        """Retrieve all amenities."""
        return self.amenity_repo.get_all()

    def get_amenity_by_name(self, name: str) -> Amenity:
        """Retrieve an amenity by its name."""
        amenities = self.amenity_repo.get_all()
        for amenity in amenities:
            if amenity.name == name:
                return amenity
        return None

    def update_amenity(self, amenity_id: str, amenity_data: dict) -> Amenity:
        """Update an amenity with the provided data."""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']
        
        self.amenity_repo.update(amenity_id, amenity)
        return amenity

    # ==================== Place Services ====================
    
    def create_place(self, place_data: dict) -> Place:
        """Create a new place with the provided data."""
        owner_id = place_data.get('owner_id')
        if not owner_id:
            raise ValueError("Place data does not contain owner_id")
        
        type_validation(owner_id, "owner_id", str)
        if not is_valid_uuid4(owner_id):
            raise ValueError("Given owner_id is not a valid UUID4")
        
        existing_user = self.user_repo.get(owner_id)
        if not existing_user:
            raise ValueError("No user corresponding to owner_id")
        
        # Prepare place data
        place_data = place_data.copy()
        place_data.pop('owner_id', None)
        place_data['owner'] = existing_user
        
        # Handle amenities
        amenities = place_data.pop('amenities', None)
        place = Place(**place_data)
        
        if amenities:
            for amenity_id in amenities:
                if not is_valid_uuid4(amenity_id):
                    raise ValueError(f"Amenity_id {amenity_id} is not a valid UUID4")
                amenity = self.get_amenity(amenity_id)
                if amenity:
                    place.add_amenity(amenity)
        
        self.place_repo.add(place)
        return place

    def get_place(self, place_id: str) -> Place:
        """Retrieve a place by its ID."""
        if not is_valid_uuid4(place_id):
            raise ValueError("Given place_id is not a valid UUID4")
        return self.place_repo.get(place_id)

    def get_all_places(self) -> list:
        """Retrieve all places."""
        return self.place_repo.get_all()

    def update_place(self, place_id: str, place_data: dict) -> Place:
        """Update a place with the provided data."""
        place = self.get_place(place_id)
        if not place:
            return None
        
        # Update owner if provided
        owner_id = place_data.get('owner_id')
        if owner_id:
            if not is_valid_uuid4(owner_id):
                raise ValueError("Given owner_id is not a valid UUID4")
            existing_user = self.get_user(owner_id)
            if not existing_user:
                raise ValueError("No user corresponding to owner_id")
            place.owner = existing_user
        
        # Update other fields
        if 'title' in place_data:
            place.title = place_data['title']
        if 'description' in place_data:
            place.description = place_data['description']
        if 'price' in place_data:
            place.price = place_data['price']
        if 'latitude' in place_data:
            place.latitude = place_data['latitude']
        if 'longitude' in place_data:
            place.longitude = place_data['longitude']
        
        # Update amenities
        amenities_ids = place_data.get('amenities')
        if amenities_ids:
            place.amenities = []
            for amenity_id in amenities_ids:
                if not is_valid_uuid4(amenity_id):
                    raise ValueError(f"Amenity_id {amenity_id} is not a valid UUID4")
                amenity = self.get_amenity(amenity_id)
                if amenity:
                    place.add_amenity(amenity)
        
        self.place_repo.update(place_id, place)
        return place

    # ==================== Review Services ====================
    
    def create_review(self, review_data: dict) -> Review:
        """Create a new review with validation."""
        user_id = review_data.get('user_id')
        if not user_id:
            raise ValueError("Review data does not contain user_id")
        
        type_validation(user_id, "user_id", str)
        if not is_valid_uuid4(user_id):
            raise ValueError("Given user_id is not a valid UUID4")
        
        place_id = review_data.get('place_id')
        if not place_id:
            raise ValueError("Review data does not contain place_id")
        
        if not is_valid_uuid4(place_id):
            raise ValueError("Given place_id is not a valid UUID4")
        
        existing_user = self.user_repo.get(user_id)
        if not existing_user:
            raise ValueError("No user corresponding to user_id")
        
        existing_place = self.place_repo.get(place_id)
        if not existing_place:
            raise ValueError("No place corresponding to place_id")
        
        # Check for existing review
        if self.get_review_by_place_and_user(place_id, user_id):
            raise ValueError("User already left a review for this place")
        
        # Prepare review data
        review_data = review_data.copy()
        review_data.pop('user_id', None)
        review_data['user'] = existing_user
        review_data.pop('place_id', None)
        review_data['place'] = existing_place
        
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id: str) -> Review:
        """Retrieve a review by its ID."""
        if not is_valid_uuid4(review_id):
            raise ValueError("Given review_id is not a valid UUID4")
        return self.review_repo.get(review_id)

    def get_all_reviews(self) -> list:
        """Retrieve all reviews."""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id: str) -> list:
        """Retrieve all reviews for a specific place."""
        if not is_valid_uuid4(place_id):
            raise ValueError("Given place_id is not a valid UUID4")
        
        place = self.get_place(place_id)
        if not place:
            return None
        return place.reviews

    def get_review_by_place_and_user(self, place_id: str, user_id: str) -> Review:
        """Retrieve a review by place and user."""
        reviews = self.get_reviews_by_place(place_id)
        if not reviews:
            return None
        for review in reviews:
            if review.user.id == user_id:
                return review
        return None

    def update_review(self, review_id: str, review_data: dict) -> Review:
        """Update a review with the provided data."""
        review = self.get_review(review_id)
        if not review:
            return None
        
        if 'text' in review_data:
            review.text = review_data['text']
        if 'rating' in review_data:
            review.rating = review_data['rating']
        
        self.review_repo.update(review_id, review)
        return review

    def delete_review(self, review_id: str) -> None:
        """Delete a review and remove it from the place's reviews list."""
        review = self.get_review(review_id)
        if not review:
            raise ValueError("Review not found")
        
        # Remove from place's reviews
        if review.place and review in review.place.reviews:
            review.place.reviews.remove(review)
        
        self.review_repo.delete(review_id)
