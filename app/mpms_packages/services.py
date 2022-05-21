import users

class Prescription:
    def __init__(
            self, patient_name, patient_id,
            patient_phone_number, prescription_id, prescription_type,
            prescription_quantity, prescription_dosage, employee_name,
            employee_number):

        self.prescription_id = prescription_id
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
            self, appointment_type, appointment_id,
            patient_name, patient_patient_id, patient_phone_number,
            employee_name, employee_number):

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
    def __init__(self, appointment):
        self.appointment = appointment

    def add_appointment ():
        pass

    def cancel_appointment ():
        pass

    def find_next_available_appointment ():
        pass