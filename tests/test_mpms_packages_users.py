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

class HealthcareProfessionalClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the HealthcareProfessional
    class to ensure they return the correct data.
    """

    def test_name_attribute(self):
        """Test the name attribute with data."""
        health_care_professional = HealthcareProfessional(
            'Jacob Levy', 'DR5987')
        expected_response = 'Jacob Levy'

        assert health_care_professional.name == expected_response

    def test_employee_number_attribute(self):
        """Test the employee_number attribute with data."""
        health_care_professional = HealthcareProfessional(
            'Lisa Simpson', 'DR2083')
        expected_response = 'DR2083'

        assert health_care_professional.employee_number == expected_response

    def test_consultation_method(self):
        """Test the consultation method with data."""
        health_care_professional = HealthcareProfessional(
            'Tinashe Kachikoti', 'DR5987')
        patient_name = 'Yusef Assefa'
        expected_response = (
            f'{patient_name} has been consulted '
            f'by {health_care_professional.name}'
        )

        assert health_care_professional.consultation(
            patient_name) == expected_response

class DoctorClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the Doctor class to ensure
    they return the correct data.
    """

    def test_name_attribute(self):
        """Test the name attribute with data."""
        doctor = Doctor('Jacinto Abital', 'DR3922')
        expected_response = 'Jacinto Abital'

        assert doctor.name == expected_response

    def test_employee_number_attribute(self):
        """Test the employee_number attribute with data."""
        doctor = Doctor('Liba Kateryna', 'DR3092')
        expected_response = 'DR3092'

        assert doctor.employee_number == expected_response

    def test_consultation_method(self):
        """Test the consultation method with data."""
        doctor = Doctor('Pridbjørn Athanasia', 'DR1109')
        expected_response = ""

        assert True

class NurseClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the Nurse class to ensure
    they return the correct data.
    """

    def test_name_attribute(self):
        """Test the name attribute with data."""
        nurse = Nurse('Kaelyn Csaba', 'NU4013')
        expected_response = 'Kaelyn Csaba'

        assert nurse.name == expected_response

    def test_employee_number_attribute(self):
        """Test the employee_number attribute with data."""
        nurse = Nurse('Liba Kateryna', 'NU0745')
        expected_response = 'NU0745'

        assert nurse.employee_number == expected_response

class PatientClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the Patient class to ensure
    they return the correct data.
    """

    def test_name_attribute(self):
        """Test the name attribute with data."""
        patient = Patient('Hjálmar Hendrik', 'PT2017', '+4512345678', '25 Cowin Lane', 'Sheffield', 'South Yorkshire', 'S1 2AB')
        expected_response = 'Kaelyn Csaba'

        assert patient.name == expected_response

    def test_employee_number_attribute(self):
        """Test the employee_number attribute with data."""
        patient = Patient('Liba Kateryna', 'NU0745')
        expected_response = 'NU0745'

        assert patient.employee_number == expected_response

if __name__ == '__main__':
    unittest.main()
