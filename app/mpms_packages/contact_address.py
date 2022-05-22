"""This module contains the Address class. The module imports
dataclasses from the standard library."""

from dataclasses import dataclass

@dataclass
class Address:
    """This class functions as a model representing an address."""
    address_line_1: str
    city: str
    county: str
    postcode: str
    address_line_2: str = None