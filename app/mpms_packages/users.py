class HealthcareProfessional:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number
    
    def consultation ():
        pass

class Doctor (HealthcareProfessional):
    def __init__(self, name, employee_number):
        super().__init__(name, employee_number)
    
    def issue_prescription ():
        pass

class Nurse (HealthcareProfessional):
    def __init__(self, name, employee_number):
        super().__init__(name, employee_number)

class Receptionist:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    def make_appointment ():
        pass

    def cancel_appointment ():
        pass

class Patient:
    def __init__(self, name, patient_id, phone_number):
        self.name = name
        self.patient_id = patient_id
        self.address = None
        self.phone_number = phone_number
    
    def request_repeat_prescription ():
        pass

    def request_appointment ():
        pass