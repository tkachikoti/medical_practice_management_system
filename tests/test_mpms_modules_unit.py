"""This module contains functions that test the functionality of the
modules inside the mpms_modules package.
This module imports a class from flaskr.flat_file_database and objects
from app.py.
"""

import unittest


class AddressModuleTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()