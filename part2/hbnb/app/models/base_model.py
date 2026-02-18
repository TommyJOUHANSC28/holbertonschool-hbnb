import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all models.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now
        self.updated_at = datetime.now

    def save(self):
        self.updated_at = self.datetime.now()

    def to_dict(self):
        return self.__dict__
