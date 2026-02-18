import uuid

class BaseModel:
    """
    Base class for all models.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())