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

class AppointmentScheduleClassTestCase(unittest.TestCase):
    """Test the attributes and methods for the AppointmentSchedule class
    to ensure they return correct data.
    """
    @classmethod
    def setUpClass(cls):
        """Set up data for the test class."""
        cls.appointment_schedule_list = []
        # Appointment 1 
        cls.patient_address_1 = Address(
            '33 Huel Lane', 'London', 'Greater London', 'SE15 2DG')
        cls.patient_1 = Patient(
            'Akhil Maria', 'PT3338', '454766628902', cls.patient_address_1)
        cls.employee_1 = HealthcareProfessional('Blaguna Gauti', 'DR5821')
        cls.appointment_schedule_list.append(Appointment(
            'Consultation', 'AP1111', '2022-06-12 at 09:00',
            cls.patient_1, cls.employee_1))

        # Appointment 2
        cls.patient_address_2 = Address(
            '123 Example Road', 'London', 'Greater London', 'N3 6SA')
        cls.patient_2 = Patient(
            'Vilmos Ianus', 'PT9999', '451118888274', cls.patient_address_2)
        cls.employee_2 = HealthcareProfessional('Anil Tony', 'DR7456')
        cls.appointment_schedule_list.append(Appointment(
            'Consultation', 'AP8356', '2022-12-01 at 12:00',
            cls.patient_2, cls.employee_2))
        
        # Appointment 3
        cls.patient_address_3 = Address(
            'Apt 72', 'Newcastle upon Tyne', 'Tyne and Wear', 'NE12 8FB',
            'Walmer House, Liverpool Street')
        cls.patient_3 = Patient(
            'Eleonora Duilius', 'PT0987', '4528563999', cls.patient_address_3)
        cls.employee_3 = HealthcareProfessional('Leolin Zion', 'DR0001')
        cls.appointment_schedule_list.append(Appointment(
            'Consultation', 'AP3298', '2023-05-17 at 16:30',
            cls.patient_3, cls.employee_3))
        
        # Appointment 4
        cls.patient_address_4 = Address(
            'Apt 22', 'York', 'North Yorkshire', 'YO12 2DR',
            'Engineer House, Plug Street')
        cls.patient_4 = Patient(
            'Carina Zemfira', 'PT8873', '454836994730', cls.patient_address_4)
        cls.employee_4 = HealthcareProfessional(
            'Gualguainus Katalinka', 'DR0003')
        
        # Appointment 5
        cls.appointment_schedule_list.append(Appointment(
            'Consultation', 'AP1991', '2023-05-17 at 16:30',
            None, cls.employee_4))

    def test_employee_name_attribute_with_data(cls) -> None:
        """Test the appointment.employee.name attribute with data."""
        appointment_schedule = AppointmentSchedule(
            cls.appointment_schedule_list)
        expected_response = "Anil Tony"

        assert (appointment_schedule.appointments[1].employee.name 
            == expected_response)
    
    def test_add_appointment_method_with_data(cls) -> None:
        """Test the add_appointment method with data."""
        appointment_schedule = AppointmentSchedule(
            cls.appointment_schedule_list)
        expected_response = "AP2222"

        appointment_schedule.add_appointment(
            'Consultation', 'AP2222', '2023-02-23 at 15:15',
            cls.patient_4, cls.employee_4)
        
        assert (appointment_schedule.appointments[-1].appointment_id 
            == expected_response)
    
    def test_cancel_appointment_method_with_data(cls) -> None:
        """Test the cancel_appointment method with data."""
        appointment_schedule = AppointmentSchedule(
            cls.appointment_schedule_list)
        expected_response = "AP3298"

        cancelled_appointment = appointment_schedule.cancel_appointment(
            'AP3298')
        
        assert (cancelled_appointment.appointment_id == expected_response)
    
    def test_find_next_available_appointment_method_with_data(cls) -> None:
        """Test the find_next_available_appointment method with data."""
        appointment_schedule = AppointmentSchedule(
            cls.appointment_schedule_list)
        expected_response = "AP1991"

        next_available_appointment = (
            appointment_schedule.find_next_available_appointment())

        assert (
            next_available_appointment.appointment_id == expected_response)

if __name__ == '__main__':
    unittest.main()
