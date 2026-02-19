"""
Repository module for data persistence
Implements an in-memory storage system for entities
"""
from abc import ABC, abstractmethod


class Repository(ABC):
    """
    Abstract base class for repository implementations.
    Defines the interface that all repositories must implement.
    """
    
    @abstractmethod
    def add(self, obj):
        """Add a new object to the repository"""
        pass
    
    @abstractmethod
    def get(self, obj_id):
        """Retrieve an object by its ID"""
        pass
    
    @abstractmethod
    def get_all(self) -> list:
        """Retrieve all objects from the repository"""
        pass
    
    @abstractmethod
    def update(self, obj_id, data):
        """Update an existing object in the repository"""
        pass
    
    @abstractmethod
    def delete(self, obj_id):
        """Delete an object from the repository"""
        pass
    
    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """Retrieve an object by a specific attribute value"""
        pass


class InMemoryRepository(Repository):
    """
    In-memory repository implementation.
    Uses a dictionary to store objects with their IDs as keys.
    """
    
    def __init__(self):
        """Initialize an empty storage dictionary"""
        self._storage = {}
    
    def add(self, obj):
        """
        Add a new object to the repository
        
        Args:
            obj: The object to add (must have an 'id' attribute)
        """
        self._storage[obj.id] = obj
    
    def get(self, obj_id):
        """
        Retrieve an object by its ID
        
        Args:
            obj_id (str): The ID of the object to retrieve
        
        Returns:
            object: The object if found, None otherwise
        """
        return self._storage.get(obj_id)
    
    def get_all(self):
        """
        Retrieve all objects from the repository
        
        Returns:
            list: List of all stored objects
        """
        return list(self._storage.values())
    
    def update(self, obj_id, data):
        """
        Update an existing object in the repository
        
        Args:
            obj_id (str): The ID of the object to update
            data (dict): Dictionary containing fields to update
        """
        obj = self.get(obj_id)
        if obj:
            obj.update(data)
    
    def delete(self, obj_id):
        """
        Delete an object from the repository
        
        Args:
            obj_id (str): The ID of the object to delete
        """
        if obj_id in self._storage:
            del self._storage[obj_id]
    
    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieve an object by a specific attribute value
        
        Args:
            attr_name (str): The name of the attribute to search by
            attr_value: The value to match
        
        Returns:
            object: The first object matching the criteria, None if not found
        """
        return next((obj for obj in self._storage.values() 
                    if getattr(obj, attr_name) == attr_value), None)
