"""This module contains functions that test the functionality of the
classes inside the users.py module.
This module imports unittest from the standard library and
users.py module from the mpms_packages.
"""

import unittest

from app.mpms_packages.contact_address import Address
from app.mpms_packages.system_users import HealthcareProfessional
from app.mpms_packages.system_users import Doctor
from app.mpms_packages.system_users import Nurse
from app.mpms_packages.system_users import Receptionist
from app.mpms_packages.system_users import Patient

class HealthcareProfessionalClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the HealthcareProfessional
    class to ensure they return the correct data.
    """
    def test_name_attribute(self) -> None:
        """Test the name attribute with data."""
        health_care_professional = HealthcareProfessional(
            'Jacob Levy', '5987')
        expected_response = 'Jacob Levy'

        assert health_care_professional.name == expected_response

    def test_employee_id_attribute(self) -> None:
        """Test the employee_id attribute with data."""
        health_care_professional = HealthcareProfessional(
            'Lisa Simpson', '2083')
        expected_response = '2083'

        assert health_care_professional.employee_id == expected_response

    def test_consultation_method(self) -> None:
        """Test the consultation method with data."""
        health_care_professional = HealthcareProfessional(
            'Tinashe Kachikoti', '5987')
        patient_name = 'Yusef Assefa'
        recommendation = 'Take a deep breath and take a deep breath.'
        expected_response = (
            f'{patient_name} has been consulted '
            f'by {health_care_professional.name}. '
            f'Recommendation: {recommendation}'
        )

        assert health_care_professional.consultation(
            patient_name, recommendation) == expected_response

class DoctorClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the Doctor class to ensure
    they return the correct data.
    """
    def test_name_attribute(self) -> None:
        """Test the name attribute with data."""
        doctor = Doctor('Jacinto Abital', '3922')
        expected_response = 'Jacinto Abital'

        assert doctor.name == expected_response

    def test_employee_id_attribute(self) -> None:
        """Test the employee_id attribute with data."""
        doctor = Doctor('Liba Kateryna', '3092')
        expected_response = '3092'

        assert doctor.employee_id == expected_response

    def test_issue_prescription_method(self) -> None:
        """Test the issue_prescription method with data."""
        doctor = Doctor('Pridbjorn Athanasia', '1109')
        expected_response = True

        assert doctor.issue_prescription() == expected_response

class NurseClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the Nurse class to ensure
    they return the correct data.
    """
    def test_name_attribute(self) -> None:
        """Test the name attribute with data."""
        nurse = Nurse('Kaelyn Csaba', '4013')
        expected_response = 'Kaelyn Csaba'

        assert nurse.name == expected_response

    def test_employee_id_attribute(self) -> None:
        """Test the employee_id attribute with data."""
        nurse = Nurse('Liba Kateryna', '745')
        expected_response = '745'

        assert nurse.employee_id == expected_response

class ReceptionistClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the Receptionist class to
    ensure they return the correct data.
    """
    def test_name_attribute(self) -> None:
        """Test the name attribute with data."""
        receptionist = Receptionist('Elmo Pranvera', '2210')
        expected_response = 'Elmo Pranvera'

        assert receptionist.name == expected_response

    def test_employee_id_attribute(self) -> None:
        """Test the employee_id attribute with data."""
        receptionist = Receptionist('Sol Mohammad', '1111')
        expected_response = '1111'

        assert receptionist.employee_id == expected_response

    def test_make_appointment_method(self) -> None:
        """Test the make_appointment method with data."""
        receptionist = Receptionist('Gergo Gracja', '2122')
        expected_response = True

        assert receptionist.make_appointment() == expected_response
    
    def test_cancel_appointment_method(self) -> None:
        """Test the cancel_appointment method with data."""
        receptionist = Receptionist('Xavi Ava', '1234')
        expected_response = True

        assert receptionist.cancel_appointment() == expected_response

class PatientClassTestCase(unittest.TestCase):
    """Test the attributes and methods of the Patient class to ensure
    they return the correct data.
    """
    def test_name_attribute(self) -> None:
        """Test the name attribute with data."""
        address = Address(
            '25 Cowin Lane','Sheffield', 'South Yorkshire', 'S1 2AB')
        patient = Patient(
            'Hjalmar Hendrik', '2017', '+4512345678', address)
        expected_response = 'Hjalmar Hendrik'

        assert patient.name == expected_response

    def test_address_postcode_attribute(self) -> None:
        """Test the address.postcode attribute with data."""
        address = Address(
            '105 East Street','Oxford', 'Oxfordshire', 'OX1 2AB')
        patient = Patient(
            'Gislenus Antonieta', '7793', '+45456456251', address)
        expected_response = 'OX1 2AB'

        assert patient.address.postcode == expected_response

    def test_request_repeat_prescription_method(self) -> None:
        """Test the request_repeat_prescription method with data."""
        address = Address(
            '2A Baker House', 'Leeds', 'West Yorkshire',
            'LS8 1IN', 'Sunny Lane')
        patient = Patient(
            'Totty Faisal', '2636', '+45283650813', address)
        expected_response = True

        assert patient.request_repeat_prescription() == expected_response
    
    def test_request_appointment_method(self) -> None:
        """Test the request_appointment method with data."""
        address = Address(
            '9 Walnut Street', 'Gateshead', 'Tyne and Wear', 'NE8 3BB')
        patient = Patient(
            'Smiljana Helena', '4927', '+45472008599', address)
        expected_response = True

        assert patient.request_appointment() == expected_response

if __name__ == '__main__':
    unittest.main()
