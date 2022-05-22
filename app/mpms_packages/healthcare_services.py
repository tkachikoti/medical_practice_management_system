"""This module contains classes that are related to the healthcare
services that are provided/consumed by the employees/patients of a
medical practice. The classes in this module are:
    - Prescription
    - Appointment
    - AppointmentSchedule

The module imports the following modules from
app.mpms_packages.system_users:
    - Patient
    - Doctor
    - HealthcareProfessional

In addition to this, the module imports the dataclasses module from
the standard library.
"""

from dataclasses import dataclass

from app.mpms_packages.system_users import Patient
from app.mpms_packages.system_users import Doctor
from app.mpms_packages.system_users import HealthcareProfessional

@dataclass
class Prescription:
    """This class functions as a model representing a prescription."""
    prescription_id: str
    prescription_type: str
    prescription_quantity: int
    prescription_dosage: str
    patient: Patient
    doctor: Doctor
    prescription_name: str = None

@dataclass
class Appointment:
    """This class functions as a model representing an appointment."""
    appointment_type: str
    appointment_id: str
    appointment_date: str
    patient: Patient
    employee: HealthcareProfessional

    def add_appointment (self) -> bool:
        return True

    def cancel_appointment (self) -> bool:
        True

    def find_next_available_appointment (self) -> bool:
        return True

class AppointmentSchedule:
    """This class functions as a model representing an appointment
    schedule.
    """
    appointment: Appointment

    def add_appointment (self) -> bool:
        return True

    def cancel_appointment (self) -> bool:
        return True

    def find_next_available_appointment (self) -> bool:
        return True
