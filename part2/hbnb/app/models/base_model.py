import uuid
import datetime

class BaseModel:
    """
    Base class for all models.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime
        self.updated_at = datetime