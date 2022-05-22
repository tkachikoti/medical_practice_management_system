"""This module contains functions that test the functionality of the
Address class inside the contact_address.py module.
This module imports unittest from the standard library and
the contact_address.py module from mpms_packages.
"""

import unittest

from app.mpms_packages.contact_address import Address

class AddressClassAttributesTestCase(unittest.TestCase):
    """Test the attributes for the Address class to ensure they return
    correct data.
    """
    def test_address_line_2_attribute_with_data(self) -> None:
        """Test the address_line_2 attribute with data."""
        address = Address(
            '64 Boyd House', 'Chatham', 'Kent', 'ME4 6JT', 'Victoria Road')
        expected_response = 'Victoria Road'

        assert address.address_line_2 == expected_response
    
    def test_address_line_2_attribute_without_data(self) -> None:
        """Test the address_line_2 attribute without data."""
        address = Address(
            '82 Riverside Road', 'London', 'Greater London', 'N1 2QP')
        expected_response = None

        assert address.address_line_2 == expected_response

    def test_county_attribute(self) -> None:
        """Test the county attribute."""
        address = Address(
            '2 Fleet Street', 'York', 'North Yorkshire', 'YO1 1AA')
        expected_response = 'North Yorkshire'

        assert address.county == expected_response

if __name__ == '__main__':
    unittest.main()
