"""This module contains functions that test the functionality of the
classes inside the users.py module.
This module imports unittest from the standard library and
users.py module from the mpms_packages.
"""

import unittest

from app.mpms_packages.users import HealthcareProfessional
from app.mpms_packages.users import Doctor
from app.mpms_packages.users import Nurse
from app.mpms_packages.users import Receptionist
from app.mpms_packages.users import Patient

class HealthcareProfessionalClassAttributesTestCase(unittest.TestCase):
    """Test the attributes of the HealthcareProfessional class to
    ensure they return the correct data."""

    def test_address_line_2_attribute_with_data(self):
        """Test the address_line_2 attribute with data."""
        address = Address(
            '64 Boyd House', 'Chatham', 'Kent', 'ME4 6JT', 'Victoria Road')
        expected_response = 'Victoria Road'
        assert address.address_line_2 == expected_response
    
    def test_address_line_2_attribute_without_data(self):
        """Test the address_line_2 attribute without data."""
        address = Address(
            '82 Riverside Road', 'London', 'Greater London', 'N1 2QP')
        expected_response = ''
        assert address.address_line_2 == expected_response

    def test_county_attribute(self):
        """Test the county attribute."""
        address = Address(
            '2 Fleet Street', 'York', 'North Yorkshire', 'YO1 1AA')
        expected_response = 'North Yorkshire'
        assert address.county == expected_response

if __name__ == '__main__':
    unittest.main()