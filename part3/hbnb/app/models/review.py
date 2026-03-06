"""
Review entity model.
Supports both object references and id references.
"""
from datetime import datetime
import uuid
from hbnb.app.models.base_model import BaseModel
from hbnb.app import db


class Review(BaseModel, db.Model):
    """Review model mapped with SQLAlchemy"""
    __tablename__ = "reviews"
    
    # ✅ UUID pour l'ID (cohérent avec Place et User)
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # 🔹 Stockage des références aux utilisateurs et lieux (UUID strings)
    user_id = db.Column(db.String(36), nullable=False)  # ✅ UUID string
    place_id = db.Column(db.String(36), nullable=False)  # ✅ UUID string
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, 
                          onupdate=datetime.utcnow, nullable=False)
    
    def __init__(self, text, rating,
                 user=None, place=None,
                 user_id=None, place_id=None, **kwargs):
        super().__init__(**kwargs)
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Review text cannot be empty")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        
        self.text = text
        self.rating = rating
        
        # Support tests (objets)
        if user and place:
            self.user = user
            self.place = place
            self.user_id = user.id
            self.place_id = place.id
        # Support API (ids seulement)
        elif user_id and place_id:
            self.user = None
            self.place = None
            self.user_id = user_id
            self.place_id = place_id
        else:
            raise ValueError("User and Place or user_id and place_id required")
    
    def __repr__(self):
        return f'<Review rating={self.rating}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "created_at": self.created_at.isoformat() if hasattr(self, 'created_at') else None,
            "updated_at": self.updated_at.isoformat() if hasattr(self, 'updated_at') else None
        }
