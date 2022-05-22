"""This module contains functions that test the functionality of the
classes inside the healthcare_services.py module.
This module imports unittest from the standard library. The module also
imports the following modules from app.mpms_packages:
    - healthcare_services
    - system_users
    - contact_address
"""

import unittest

from app.mpms_packages.healthcare_services import Prescription
from app.mpms_packages.healthcare_services import Appointment
from app.mpms_packages.healthcare_services import AppointmentSchedule
from app.mpms_packages.system_users import Patient
from app.mpms_packages.system_users import Doctor
from app.mpms_packages.contact_address import Address

class PrescriptionClassTestCase(unittest.TestCase):
    """Test the attributes and methods for the Prescription class
    to ensure they return correct data.
    """
    def test_prescription_type_attribute_with_data(self) -> None:
        """Test the prescription_type attribute with data."""
        patient_address = Address(
            '82 Riverside Road', 'London', 'Greater London', 'N1 2QP')
        patient = Patient(
            'Judy Mette', 'PT4872', '450394817894', patient_address)
        doctor = Doctor('Zaya Taline', 'DR4999')
        prescription = Prescription(
            'PS3864', 'Tablet', '10', '1 tablet a day',
            patient, doctor, 'Paracetamol')
        expected_response = 'Tablet'

        assert prescription.prescription_type == expected_response
    
    def test_address_line_2_attribute_with_data(self) -> None:
        """Test the patient.address.address_line_2 attribute with data.
        """
        patient_address = Address(
            '11 Steel Mill House', 'London', 'Greater London',
            'SW1P 1AA', 'Opiumpark Lane')
        patient = Patient(
            'Maximilian Zaida', 'PT3902', '453789268490', patient_address)
        doctor = Doctor('Frej Gili', 'DR4928')
        prescription = Prescription(
            'PS3902', 'Tablet', '60', '2 tablet a day',
            patient, doctor, 'Acrivastine')
        expected_response = 'Opiumpark Lane'

        assert (
            prescription.patient.address.address_line_2 == expected_response)

if __name__ == '__main__':
    unittest.main()
