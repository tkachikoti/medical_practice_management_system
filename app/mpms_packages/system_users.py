"""This module contains the classes that represent the users of a
medical practice management system. The module uses the Address class
from the contact_address.py module.
"""

from dataclasses import dataclass

from app.mpms_packages.contact_address import Address

@dataclass
class HealthcareProfessional:
    """This dataclass functions as a model representing a healthcare 
    professional.
    """
    name: str
    employee_number: str
    
    def consultation(self, patient_name: str, recommendation: str) -> str:
        """This method returns a string containing the patient name,
        the healthcare professional name and the recommendation.
        :param patient_name: The name of the patient.
        :type patient_name: str
        :param recommendation: The recommendation for the patient.
        :type recommendation: str
        :return: A string containing the patient name, the healthcare
        professional name and the recommendation.
        :rtype: str
        """
        return (
            f'{patient_name} has been consulted by {self.name}. '
            f'Recommendation: {recommendation}')

@dataclass
class Doctor(HealthcareProfessional):
    """This class functions as a model representing a doctor.
    It inherits the attributes and methods of the HealthcareProfessional
    dataclass.
    """
    name: str
    employee_number: str

    def __post_init__(self):
        """This method post-initializes the Doctor class. It sets the
        name and employee number attributes.
        :param name: The name of the doctor.
        :type name: str
        :param employee_number: The employee number of the doctor.
        :type employee_number: str
        """
        super().__init__(self.name, self.employee_number)

    def issue_prescription(self) -> bool:
        return True

@dataclass
class Nurse(HealthcareProfessional):
    """This class functions as a model representing a nurse.
    It inherits the attributes and methods of the HealthcareProfessional
    dataclass.
    """
    name: str
    employee_number: str

    def __post_init__(self):
        """This method post-initializes the Nurse class. It sets the name
        and employee number attributes.
        :param name: The name of the nurse.
        :type name: str
        :param employee_number: The employee number of the nurse.
        :type employee_number: str
        """
        super().__init__(self.name, self.employee_number)

@dataclass
class Receptionist:
    """This class functions as a model representing a receptionist."""
    name: str
    employee_number: str

    def make_appointment(self) -> bool:
        return True

    def cancel_appointment(self) -> bool:
        return True

@dataclass
class Patient:
    """This class functions as a model representing a patient."""
    name: str
    patient_id: str
    phone_number: int
    address: Address
    
    def request_repeat_prescription(self) -> bool:
        return True

    def request_appointment(self) -> bool:
        return True
