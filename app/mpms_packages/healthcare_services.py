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

In addition to this, the module imports the dataclasses and datetime
modules from the standard library.
"""

from dataclasses import dataclass

from app.mpms_packages.system_users import Patient
from app.mpms_packages.system_users import Doctor
from app.mpms_packages.system_users import HealthcareProfessional

@dataclass
class Prescription:
    """This class functions as a model representing a prescription."""
    prescription_id: int
    prescription_type: str
    prescription_quantity: int
    prescription_dosage: str
    patient: Patient
    doctor: Doctor
    prescription_name: str = None

@dataclass
class Appointment:
    """This class functions as a model representing an appointment."""
    appointment_type: str = None
    appointment_id: int = None
    appointment_date: str = None
    patient: Patient = None
    employee: HealthcareProfessional = None

@dataclass
class AppointmentSchedule:
    """This class functions as a model representing an appointment
    schedule.
    """
    appointments: list

    def add_appointment(
            self, appointment_type: str, appointment_id: int,
            appointment_date: str, patient: Patient,
            employee: HealthcareProfessional) -> Appointment:
        """This method adds an appointment to the appointment schedule
        and returns the appointment.
        :param appointment_type: The type of appointment.
        :type appointment_type: str
        :param appointment_id: The id of the appointment.
        :type appointment_id: int
        :param appointment_date: The date of the appointment.
        :type appointment_date: str
        :param patient: The patient of the appointment.
        :type patient: Patient
        :param employee: The employee of the appointment.
        :type employee: HealthcareProfessional
        :return: The appointment that was added to the appointment
        schedule.
        :rtype: Appointment
        """
        new_appointment = Appointment(
            appointment_type, appointment_id, appointment_date,
            patient, employee)
        self.appointments.append(new_appointment)
        return new_appointment

    def cancel_appointment(self, appointment_id: int) -> Appointment:
        """This method cancels an appointment from the appointment
        schedule and returns the appointment.
        :param appointment_id: The id of the appointment to be
        cancelled.
        :type appointment_id: int
        :return: The appointment that was cancelled from the
        appointment schedule.
        :rtype: Appointment
        """
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                self.appointments.remove(appointment)
                return appointment

    def find_next_available_appointment(self) -> Appointment:
        """This method finds the next available appointment from the
        appointment schedule and returns the appointment.
        :return: The next available appointment from the appointment
        schedule.
        :rtype: Appointment
        """
        for appointment in self.appointments:
            if appointment.patient is None:
                return appointment
