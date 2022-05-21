import users

class Prescription:
    def __init__(self, **prescription_data, **patient_data, **staff_data):
        self.prescription_id = prescription_data.prescription_id
        self.prescription_type = prescription_data.prescription_type
        self.patient = users.Patient(
            patient_data.name,
            patient_data.patient_id,
            patient_data.phone_number)
        self.doctor = users.Doctor(
            staff_data.name,
            staff_data.employee_number)
        self.quantity = prescription_data.quantity
        self.dosage = prescription_data.dosage

class Appointment:
    def __init__(
            self, appointment_type, appointment_id,
            **patient_data, **staff_data):
        self.appointment_type = appointment_type
        self.appointment_id = None
        self.patient = users.Patient(
            patient_data.name,
            patient_data.patient_id,
            patient_data.phone_number)
        self.staff = users.Healthcare_professional(
            staff_data.name,
            staff_data.employee_number)

    def add_appointment ():
        pass

    def cancel_appointment ():
        pass

    def find_next_available_appointment ():
        pass

class Appointment_schedule:
    def __init__(self, appointment):
        self.appointment = appointment

    def add_appointment ():
        pass

    def cancel_appointment ():
        pass

    def find_next_available_appointment ():
        pass