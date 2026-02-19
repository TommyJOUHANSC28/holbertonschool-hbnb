"""
Persistence layer package.

Provides access to repository implementations.
"""

from .repository import InMemoryRepository

__all__ = ["InMemoryRepository"]
