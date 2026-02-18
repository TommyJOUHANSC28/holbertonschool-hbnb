#!/usr/bin/python3
from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.places import Place
from app.models.reviews import Review
from app.models.amenities import Amenity


class HBnBFacade:

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ==========================
    # USER METHODS
    # ==========================

    def create_user(self, data):
        if self.user_repo.get_by_attribute("email", data["email"]):
            raise ValueError("Email already exists")

        user = User(**data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def delete_user(self, user_id):
        return self.user_repo.delete(user_id)

    # ==========================
    # PLACE METHODS
    # ==========================

    def create_place(self, data):
        owner = self.user_repo.get(data["owner_id"])
        if not owner:
            raise ValueError("Owner not found")

        place = Place(**data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def delete_place(self, place_id):
        return self.place_repo.delete(place_id)

    # ==========================
    # REVIEW METHODS
    # ==========================

    def create_review(self, data):
        user = self.user_repo.get(data["user_id"])
        place = self.place_repo.get(data["place_id"])

        if not user:
            raise ValueError("User not found")

        if not place:
            raise ValueError("Place not found")

        review = Review(**data)
        self.review_repo.add(review)
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    # ==========================
    # AMENITY METHODS
    # ==========================

    def create_amenity(self, data):
        amenity = Amenity(**data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()
