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
from app.mpms_packages.system_users import HealthcareProfessional
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

class AppointmentClassTestCase(unittest.TestCase):
    """Test the attributes and methods for the Appointment class
    to ensure they return correct data.
    """
    def test_appointment_id_attribute_with_data(self) -> None:
        """Test the appointment_id attribute with data."""
        patient_address = Address(
            '5 Mazzaline Road', 'London', 'Greater London', 'E1 6QP')
        patient = Patient(
            'Shauna Oshrat', 'PT5924', '4539457626908', patient_address)
        employee = HealthcareProfessional('Caroline Ido', 'DR4899')
        appointment = Appointment(
            'Consultation', 'AP3298', '2023-02-06 at 14:00',
            patient, employee)
        expected_response = 'AP3298'

        assert appointment.appointment_id == expected_response
    
    def test_postcode_attribute_with_data(self) -> None:
        """Test the patient.address.postcode attribute with data.
        """
        patient_address = Address(
            '78 Waterfalls Avenue', 'London', 'Greater London', 'W3 1QP')
        patient = Patient(
            'Bratislava Silvia', 'PT6631', '459876420555', patient_address)
        employee = HealthcareProfessional('Dakila Mitra', 'DR7777')
        appointment = Appointment(
            'Consultation', 'AP3298', '2023-02-06 at 14:00',
            patient, employee)
        expected_response = 'W3 1QP'

        assert (
            appointment.patient.address.postcode == expected_response)

if __name__ == '__main__':
    unittest.main()
