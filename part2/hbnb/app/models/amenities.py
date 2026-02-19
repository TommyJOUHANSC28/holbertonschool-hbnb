"""
Amenity model module
"""
from app.models.baseEntity import (BaseEntity, type_validation,
                                   strlen_validation)


class Amenity(BaseEntity):
    """
    Amenity class represents an amenity/feature available at a place
    Inherits from BaseEntity for common attributes (id, created_at, updated_at)
    """
    
    def __init__(self, name: str):
        """
        Initialize an Amenity instance
        
        Args:
            name (str): Name of the amenity
        """
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = self.validate_name(value)

    def validate_name(self, name):
        """Verify if the name is a string with valid length."""
        if not name:
            raise ValueError("Name is required")
        type_validation(name, "Name", str)
        name = name.strip()
        strlen_validation(name, "Name", 1, 50)
        return name

    # def to_dict(self):
    #     """Convert the Amenity object to a dictionary representation,
    #     including BaseEntity fields"""
    #     base_dict = super().to_dict()
    #     base_dict.update({
    #         "name": self.name
    #     })
    #     return base_dict
