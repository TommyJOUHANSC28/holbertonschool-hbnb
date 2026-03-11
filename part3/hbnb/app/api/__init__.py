"""API v1 Blueprint initialization."""
from flask import Blueprint

api_v1_bp = Blueprint('api_v1', __name__)

# Import routes after blueprint creation to avoid circular imports
from hbnb.app.api.v1 import users

__all__ = ['api_v1_bp']
