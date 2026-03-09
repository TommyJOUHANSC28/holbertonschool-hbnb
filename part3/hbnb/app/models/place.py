"""
Place model.
Represents a place/accommodation in the system.
"""
from datetime import datetime
import uuid
from hbnb.app.models.base_model import BaseModel
from hbnb.app import db


class Place(BaseModel, db.Model):
    """Place model mapped with SQLAlchemy"""
    __tablename__ = "places"
    
    # ✅ UUID pour l'ID
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), 
                        nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, 
                          onupdate=datetime.utcnow, nullable=False)
    
    # =========================================================================
    # RELATIONS
    # =========================================================================
    
    # Many-to-One: Une place appartient à un utilisateur (propriétaire)
    owner = db.relationship(
        'User',
        back_populates='places',
        lazy='select',
        foreign_keys=[owner_id]
    )
    
    # One-to-Many: Une place peut avoir plusieurs reviews
    reviews = db.relationship(
        'Review',
        back_populates='place',
        cascade='all, delete-orphan',
        lazy='select',
        foreign_keys='Review.place_id'
    )
    
    def __init__(self, title, description, price, latitude, longitude, owner_id, **kwargs):
        """
        Initialize Place with required fields.
        
        Args:
            title (str): Title of the place
            description (str): Description of the place
            price (float): Price per night
            latitude (float): Latitude coordinate
            longitude (float): Longitude coordinate
            owner_id (str): ID of the owner (User)
        """
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
    
    def __repr__(self):
        return f'<Place {self.title}>'
    
    def to_dict(self, include_owner=False, include_reviews=False):
        """
        Convert place to dictionary
        
        Args:
            include_owner: Include owner details
            include_reviews: Include reviews list
        """
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat() if hasattr(self, 'created_at') else None,
            'updated_at': self.updated_at.isoformat() if hasattr(self, 'updated_at') else None
        }
        
        if include_owner and self.owner:
            data['owner'] = self.owner.to_dict()
        
        if include_reviews and self.reviews:
            data['reviews'] = [review.to_dict() for review in self.reviews]
        
        return data
    
    def update(self, data):
        """Update place attributes"""
        # Champs autorisés à être mis à jour
        allowed_fields = ['title', 'description', 'price', 'latitude', 'longitude']
        
        for key, value in data.items():
            if hasattr(self, key) and key in allowed_fields and key != 'id':
                setattr(self, key, value)
