"""
In-memory repository implementation.
Used for temporary storage before database integration.
"""


class InMemoryRepository:
    """
    Generic repository for storing entities in memory.
    """

    def __init__(self):
        self._storage = {}

    def add(self, obj):
        """
        Adds object to storage.
        """
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """
        Retrieves object by ID.
        """
        return self._storage.get(obj_id)

    def get_all(self):
        """
        Returns all stored objects.
        """
        return list(self._storage.values())

    def delete(self, obj_id):
        """
        Deletes object from storage.
        """
        if obj_id in self._storage:
            del self._storage[obj_id]
