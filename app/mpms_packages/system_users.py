"""This module contains the HealthcareProfessional class.
"""
from app.mpms_packages.contact_address import Address

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
    
    def issue_prescription (self) -> bool:
        return True

class Nurse (HealthcareProfessional):
    def __init__(self, name: str, employee_number: str) -> None:
        super().__init__(name, employee_number)

class Receptionist:
    def __init__(self, name: str, employee_number: str) -> None:
        self.name = name
        self.employee_number = employee_number

    def make_appointment (self) -> bool:
        return True

    def cancel_appointment (self) -> bool:
        return True

class Patient:
    def __init__(
            self, name: str, patient_id: str,
            phone_number: int, address: Address) -> None:
        self.name = name
        self.patient_id = patient_id
        self.phone_number = phone_number
        self.address = address
    
    def request_repeat_prescription (self) -> bool:
        return True

    def request_appointment (self) -> bool:
        return True