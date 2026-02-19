"""
User model module
"""
from app.models.baseEntity import (BaseEntity, type_validation,
                                   strlen_validation)
from validate_email_address import validate_email
import re


class User(BaseEntity):
    """
    User class represents a user in the HBNB application
    Inherits from BaseEntity for common attributes (id, created_at, updated_at)
    """
    
    def __init__(self, first_name: str, last_name: str,
                 email: str, is_admin: bool = False):
        """
        Initialize a User instance
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            email (str): User's email address
            is_admin (bool): Whether the user has admin privileges
        """
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
    
    def name_validation(self, names: str, names_name: str):
        """
        Validate name fields (first_name, last_name)
        
        Args:
            names (str): The name to validate
            names_name (str): The field name for error messages
            
        Returns:
            str: Cleaned and validated name
            
        Raises:
            ValueError: If name is invalid
        """
        type_validation(names, names_name, str)
        names = names.strip()
        strlen_validation(names, names_name, 1, 50)
        names_list = names.split()
        for name in names_list:
            if not re.match(r"^[^\W\d_]+([.'-][^\W\d_]+)*[.]?$", name,
                            re.UNICODE):
                raise ValueError(f"Invalid {names_name}: {names_name} "
                                 "must contain only letters, "
                                 "apostrophes, dashes, or dots (no "
                                 "digits or other special characters)")
        return " ".join(names_list)
    
    def email_validation(self, email: str):
        """
        Validate email address
        
        Args:
            email (str): The email to validate
            
        Returns:
            str: Validated email
            
        Raises:
            ValueError: If email is invalid
        """
        type_validation(email, "email", str)
        if not validate_email(email):
            raise ValueError("Invalid email: email must have format"
                             " example@exam.ple")
        return email
    
    @property
    def first_name(self):
        """Get first name"""
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        """Set and validate first name"""
        self.__first_name = self.name_validation(first_name,
                                                 "first_name")
    
    @property
    def last_name(self):
        """Get last name"""
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name):
        """Set and validate last name"""
        self.__last_name = self.name_validation(last_name, "last_name")
    
    @property
    def email(self):
        """Get email"""
        return self.__email
    
    @email.setter
    def email(self, email: str):
        """Set and validate email"""
        self.__email = self.email_validation(email)
    
    @property
    def is_admin(self):
        """Get admin status"""
        return self.__is_admin
    
    @is_admin.setter
    def is_admin(self, is_admin: bool):
        """Set and validate admin status"""
        type_validation(is_admin, "is_admin", bool)
        self.__is_admin = is_admin
