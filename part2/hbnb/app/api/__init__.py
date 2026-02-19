from flask_restx import Namespace
from app.api import ns as users_ns
from .places import ns as places_ns
from .reviews import ns as reviews_ns
from .amenities import ns as amenities_ns

def register_namespaces(api):
    api.add_namespace(users_ns, path="/users")
    api.add_namespace(places_ns, path="/places")
    api.add_namespace(reviews_ns, path="/reviews")
    api.add_namespace(amenities_ns, path="/amenities")
