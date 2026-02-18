from app.persistence.repository import InMemoryRepository
from app.models import users, places, amenities, reviews



class HBnBFacade:
    def __init__(self):
        self.user_service = UserService()
        self.place_service = PlaceService()
        self.review_service = ReviewService()
        self.amenity_service = AmenityService()

        self.user_repository = InMemoryRepository()
        self.place_repository = InMemoryRepository()
        self.review_repository = InMemoryRepository()
        self.amenity_repository = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user_data = User(**user_data)
        self.user_repository.add(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        place = self.place_repository.get(place_id)
        if place:
            place.reviews = self.review_repository.get_by_attribute('place_id', place_id)
        return place

    def get_user(self, user_id):
        user = self.user_repository.get(user_id)
        if user:
            user.reviews = self.review_repository.get_by_attribute('user_id', user_id)
        return user

    def get_place_by_user(self, user_id, place_id):
        user_id = self.user_repository.get(user_id)
        user = self.get_user(user_id)
        place_id = self.get_place(place_id)
        place = self.place_repository.get(place_id)

facade = HBnBFacade()
