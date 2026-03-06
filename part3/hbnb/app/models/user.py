"""
User model.
Represents a user in the system.
"""
from datetime import datetime
import uuid
from hbnb.app.models.base_model import BaseModel
from hbnb.app import db
from hbnb.app.utils import check_password


class User(BaseModel, db.Model):
    """User model mapped with SQLAlchemy"""
    __tablename__ = "users"
    
    # ✅ UUID pour l'ID (cohérent avec Place et Review)
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, 
                          onupdate=datetime.utcnow, nullable=False)
    
    def __init__(self, first_name, last_name, email, password, is_admin=False, **kwargs):
        super().__init__(**kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password  # Should be hashed before storage
        self.is_admin = is_admin
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    def to_dict(self):
        """Convert user to dictionary, excluding password"""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat() if hasattr(self, 'created_at') else None,
            'updated_at': self.updated_at.isoformat() if hasattr(self, 'updated_at') else None
            # Password is intentionally excluded for security
        }
    
    def verify_password(self, password):
        """
        Verify if the provided password matches the hashed password.
        Args:
            password (str): Plain text password to verify
        Returns:
            bool: True if password matches, False otherwise
        """
        return check_password(self.password, password)
    
    def update(self, data):
        """Update user attributes"""
        for key, value in data.items():
            if hasattr(self, key) and key != 'id':  # Don't allow ID updates
                setattr(self, key, value)
