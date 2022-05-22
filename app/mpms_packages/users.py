"""This module contains the HealthcareProfessional class.
"""
from services import Prescription
from address import Address

class HealthcareProfessional:
    def __init__(self, name: str, employee_number: str) -> None:
        self.name = name
        self.employee_number = employee_number
    
    def consultation (self, patient_name: str, recommendation: str) -> str:
        return (
            f'{patient_name} has been consulted by {self.name}. '
            f'Recommendation: {recommendation}')

class Doctor (HealthcareProfessional):
    def __init__(self, name: str, employee_number: str) -> None:
        super().__init__(name, employee_number)
    
    def issue_prescription ():
        pass

class Nurse (HealthcareProfessional):
    def __init__(self, name: str, employee_number: str) -> None:
        super().__init__(name, employee_number)

class Receptionist:
    def __init__(self, name: str, employee_number: str) -> None:
        self.name = name
        self.employee_number = employee_number

    def make_appointment ():
        pass

    def cancel_appointment ():
        pass

class Patient:
    def __init__(
            self, name: str, patient_id: str, phone_number: int,
            address_line_1: str, city: str, county: str, postcode: str,
            address_line_2='') -> None:
        self.name = name
        self.patient_id = patient_id
        self.address = Address(
            address_line_1, city,county, postcode, address_line_2)
        self.phone_number = phone_number
    
    def request_repeat_prescription ():
        pass

    def request_appointment ():
        pass