"""
User model module
"""
from app.models.base_model  import BaseModel


class User(BaseModel):
    """
    User class represents a user in the HBNB application
    Inherits from BaseModel for common attributes (id, created_at, updated_at)
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
        # Use setters to trigger validation
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
    
    def name_validation(self, name: str, field_name: str) -> str:
        """
        Validate name fields (first_name, last_name)

        Args:
            name (str): The name to validate
            field_name (str): The field name for error messages

        Returns:
            str: Cleaned and validated name

        Raises:
            ValueError: If name is invalid
        """
        type_validation(name, field_name, str)

        # Strip whitespace
        name = name.strip()

        # Validate length (1 to 50 characters)
        strlen_validation(name, field_name, 1, 50)

        # Validate format: only letters, apostrophes, dashes, dots, and spaces
        # Updated regex to properly handle names with spaces and special chars
        if not re.match(r"^(?!.*[\s]{2,})[^\W\d_]+(?:[.'-][^\W\d_]+)*\.?$",
                        name, re.UNICODE):
            raise ValueError(f"Invalid {field_name}: must contain only letters, "
                             "apostrophes, dashes, or dots (no digits or "
                             "other special characters)")

        return name

    def email_validation(self, email: str) -> str:
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

        # Strip whitespace from email
        email = email.strip()

        if not validate_email(email):
            raise ValueError("Invalid email address format")

        return email

    @property
    def first_name(self) -> str:
        """Get first name"""
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """Set and validate first name"""
        self.__first_name = self.name_validation(first_name, "first_name")

    @property
    def last_name(self) -> str:
        """Get last name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """Set and validate last name"""
        self.__last_name = self.name_validation(last_name, "last_name")

    @property
    def email(self) -> str:
        """Get email"""
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        """Set and validate email"""
        self.__email = self.email_validation(email)

    @property
    def is_admin(self) -> bool:
        """Get admin status"""
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin: bool) -> None:
        """Set and validate admin status"""
        type_validation(is_admin, "is_admin", bool)
        self.__is_admin = is_admin

    def __repr__(self) -> str:
        """Return string representation of User"""
        return (f"User({self.first_name!r}, {self.last_name!r}, "
                f"{self.email!r}, is_admin={self.is_admin})")
