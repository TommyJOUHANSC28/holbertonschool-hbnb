"""
Services package.

Initializes the Facade singleton instance.
"""

from .facade import HBnBFacade

# Singleton instance of the Facade
facade = HBnBFacade()

__all__ = ["facade", "HBnBFacade"]
