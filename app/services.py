class Healthcare_professional:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number
    
    def consultation ():
        pass

class Doctor (Healthcare_professional):
    def __init__(self, name, employee_number):
        super().__init__(name, employee_number)
    
    def issue_prescription ():
        pass

class Nurse (Healthcare_professional):
    def __init__(self, name, employee_number):
        super().__init__(name, employee_number)

class Prescription:
    def __init__(self, prescription_type, dosage):
        self.prescription_type = type
        self.patient = "CLASS PATIENT"