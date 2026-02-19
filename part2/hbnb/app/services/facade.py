"""
Facade layer coordinating API and business logic.
"""

from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    """
    Central facade class.
    """

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ================= USERS =================

    def create_user(self, data):
        user = User(**data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    # ================= AMENITIES =================

    def create_amenity(self, data):
        amenity = Amenity(**data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    # ================= PLACES =================

    def create_place(self, data):
        owner = self.user_repo.get(data["owner_id"])
        if not owner:
            raise ValueError("Owner not found")

        place = Place(
            title=data["title"],
            description=data.get("description"),
            price=data["price"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            owner=owner
        )

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    # ================= REVIEWS =================

    def create_review(self, data):
        user = self.user_repo.get(data["user_id"])
        place = self.place_repo.get(data["place_id"])

        if not user:
            raise ValueError("User not found")

        if not place:
            raise ValueError("Place not found")

        review = Review(
            text=data["text"],
            rating=data["rating"],
            user=user,
            place=place
        )

        place.add_review(review)
        self.review_repo.add(review)
        return review

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
