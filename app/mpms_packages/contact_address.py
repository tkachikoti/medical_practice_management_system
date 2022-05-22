"""This module contains the Address class. The module imports
dataclasses from the standard library."""

from dataclasses import dataclass

@dataclass
class Address:
    """This class contains the attributes Address dataclass."""
    address_line_1: str
    city: str
    county: str
    postcode: str
    address_line_2: str = None