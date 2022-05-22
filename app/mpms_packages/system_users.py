"""This module contains the HealthcareProfessional class. The module
uses the Address class from the contact_address.py module.
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
    
    def consultation (self, patient_name: str, recommendation: str) -> str:
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

class Doctor (HealthcareProfessional):
    """This class functions as a model representing a doctor.
    It inherits the attributes and methods of the HealthcareProfessional
    dataclass.
    """
    def __init__(self, name: str, employee_number: str) -> None:
        """This method initializes the Doctor class. It sets the name
        and employee number attributes.
        :param name: The name of the doctor.
        :type name: str
        :param employee_number: The employee number of the doctor.
        :type employee_number: str
        """
        super().__init__(name, employee_number)
    
    def issue_prescription (self) -> bool:
        return True

class Nurse (HealthcareProfessional):
    """This class functions as a model representing a nurse.
    It inherits the attributes and methods of the HealthcareProfessional
    dataclass."""
    def __init__(self, name: str, employee_number: str) -> None:
        """This method initializes the Nurse class. It sets the name
        and employee number attributes.
        :param name: The name of the nurse.
        :type name: str
        :param employee_number: The employee number of the nurse.
        :type employee_number: str
        """
        super().__init__(name, employee_number)

class Receptionist:
    """This class functions as a model representing a receptionist."""
    def __init__(self, name: str, employee_number: str) -> None:
        """This method initializes the Receptionist class. It sets the
        name and employee number attributes.
        :param name: The name of the receptionist.
        :type name: str
        :param employee_number: The employee number of the receptionist.
        :type employee_number: str
        """
        self.name = name
        self.employee_number = employee_number

    def make_appointment (self) -> bool:
        return True

    def cancel_appointment (self) -> bool:
        return True

class Patient:
    """This class functions as a model representing a patient."""
    def __init__(
            self, name: str, patient_id: str,
            phone_number: int, address: Address) -> None:
        """This method initializes the Patient class. It sets the name,
        patient id, phone number and address attributes.
        :param name: The name of the patient.
        :type name: str
        :param patient_id: The patient id of the patient.
        :type patient_id: str
        :param phone_number: The phone number of the patient.
        :type phone_number: int
        :param address: The address of the patient.
        :type address: Address
        """
        self.name = name
        self.patient_id = patient_id
        self.phone_number = phone_number
        self.address = address
        self.name = name
        self.patient_id = patient_id
        self.phone_number = phone_number
        self.address = address
    
    def request_repeat_prescription (self) -> bool:
        return True

    def request_appointment (self) -> bool:
        return True