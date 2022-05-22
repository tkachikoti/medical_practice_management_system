import users

class Prescription:
    def __init__(
            self, patient_name: str, patient_id: str,
            patient_phone_number: int, prescription_id: str,
            prescription_type: str, prescription_quantity: int, prescription_dosage: str,
            employee_name: str, employee_number: str, prescription_name='') -> None:

        self.prescription_id = prescription_id
        self.prescription_name = prescription_name
        self.prescription_type = prescription_type
        self.quantity = prescription_quantity
        self.dosage = prescription_dosage

        self.patient = users.Patient(
            patient_name,
            patient_id,
            patient_phone_number)

        self.doctor = users.Doctor(
            employee_name,
            employee_number)

class Appointment:
    def __init__(
            self, appointment_type: str, appointment_id: str,
            patient_name: str, patient_patient_id: str, patient_phone_number: int,
            employee_name: str, employee_number: str) -> None:

        self.appointment_type = appointment_type
        self.appointment_id = appointment_id

        self.patient = users.Patient(
            patient_name,
            patient_patient_id,
            patient_phone_number)

        self.staff = users.HealthcareProfessional(
            employee_name,
            employee_number)

    def add_appointment ():
        pass

    def cancel_appointment ():
        pass

    def find_next_available_appointment ():
        pass

class AppointmentSchedule:
    def __init__(self, appointment: Appointment) -> None:
        self.appointment = appointment

    def add_appointment ():
        pass

    def cancel_appointment ():
        pass

    def find_next_available_appointment ():
        pass