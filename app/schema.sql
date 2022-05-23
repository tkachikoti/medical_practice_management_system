DROP TABLE IF EXISTS system_role;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS appointment;
DROP TABLE IF EXISTS prescription;

CREATE TABLE system_role (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  role TEXT NOT NULL
);

INSERT INTO system_role (role)
VALUES
('Doctor'),
('Nurse'),
('Receptionist');

CREATE TABLE employee (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  system_role_id INTEGER NOT NULL,
  FOREIGN KEY (system_role_id) REFERENCES system_role (id)
);

INSERT INTO employee (name, system_role_id)
VALUES
('Lucjan Dina', 1),
('Iacopo Kerenza', 1),
('Nadia Steinunn', 2),
('Aglaia Imrich', 2),
('Moss Pavo', 3);

CREATE TABLE address (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address_line_1 TEXT NOT NULL,
  address_line_2 TEXT NULL,
  city TEXT NOT NULL,
  county TEXT NOT NULL,
  postcode TEXT NOT NULL
);

INSERT INTO address (address_line_1, address_line_2, city, county, postcode)
VALUES
('12 Treat Close', NULL, "London", "Greater London", "E8 3MP"),
('101 Brick Lane', NULL, "London", "Greater London", "E8 2QW");

CREATE TABLE patient (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address_id INTEGER NOT NULL,
  name TEXT UNIQUE NOT NULL,
  phone_number INTEGER NOT NULL,
  FOREIGN KEY (address_id) REFERENCES address (id)
);

INSERT INTO patient (address_id, name, phone_number)
VALUES
(1, 'Gerda Sem', 447930297712),
(2, 'Mirja Kirk', 44712309811);

CREATE TABLE appointment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER NULL,
  employee_id INTEGER NULL,
  appointment_date TEXT NULL,
  appointment_type TEXT NULL,
  FOREIGN KEY (patient_id) REFERENCES patient (id),
  FOREIGN KEY (employee_id) REFERENCES employee (id)
);

INSERT INTO appointment (patient_id, employee_id, appointment_date, appointment_type)
VALUES
(NULL, 1, '23 May 2022 at 13:00 GMT', 'Consultation'),
(NULL, 2, '25 May 2022 at 16:30 GMT', 'Consultation'),
(NULL, 3, '27 May 2022 at 09:10 GMT', NULL);

CREATE TABLE prescription (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER NULL,
  employee_id INTEGER NULL,
  prescription_quantity INTEGER NOT NULL,
  prescription_dosage TEXT NOT NULL,
  prescription_type TEXT NOT NULL,
  prescription_name TEXT NULL,
  FOREIGN KEY (patient_id) REFERENCES patient (id),
  FOREIGN KEY (employee_id) REFERENCES employee (id)
);