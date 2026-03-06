"""
Amenity model.
"""
from datetime import datetime
import uuid
from hbnb.app.models.base_model import BaseModel
from hbnb.app import db


class Amenity(BaseModel, db.Model):
    """Amenity model mapped with SQLAlchemy"""
    __tablename__ = 'amenities'
    
    # ✅ UUID pour l'ID (cohérent avec User, Place, Review)
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, 
                          onupdate=datetime.utcnow, nullable=False)
    
    def __init__(self, name, description=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'<Amenity {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if hasattr(self, 'created_at') else None,
            'updated_at': self.updated_at.isoformat() if hasattr(self, 'updated_at') else None
        }
