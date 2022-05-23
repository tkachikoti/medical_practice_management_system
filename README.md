# Medical Practice Management System

This repository contains an assignment for a Computer Science MSc module at the University of Essex.

## Table of contents

- [Description](#description)
- [Installing and running the app](#installing-and-running-the-app)
- [Testing the app](#testing-the-app)
- [References](#references)

## Description

A Medical Practice Management System (MPMS) is a system that facilitates the day-to-day operations of a medical practice (Heath, et al. 2017). The primary focus of the MPMS in this repository is to provide service users and providers an interface that makes the process of engagement as smooth as possible.

This repository contains a minimum viable product of a [Flask](https://github.com/pallets/flask) based MPMS.
- The front end interface was built using [Bootstrap](https://github.com/twbs/bootstrap) and [Jinja](https://github.com/pallets/jinja)
- The database was implemented using [SQLite 3](https://github.com/sqlite/sqlite) via a Python standard library [DB-API 2.0](https://docs.python.org/3/library/sqlite3.html)
- The testing functionality was implemented using [pytest](https://github.com/pytest-dev/pytest)

## Installing and running the app

### Codio IDE (Ubuntu 18.04.3 LTS)

1. Clone the repository:

```
$ git clone https://github.com/tkachikoti/medical_practice_management_system
```

2. Change directory:

```
$ cd medical_practice_management_system
```

3. Configure the environment and install dependencies:

```
$ sudo apt-get update
$ sudo apt-get install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -U flask
$ pip install -U pytest
$ pip install -U numpy
```

4. Run the app:

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask init-db
$ flask run
```

5. On the menu bar, click on the downward pointing chevron to open the preview menu. Please ensure that the 'Box URL' and the 'New Browser Tab' options are selected.

![The configuration that is required for the BTS app to run on Codio](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/bug-tracking-system/codio_config_1.png)

6. Click the 'Box URL' button to open a browser tab running the app.

![The button the must be clicked to open a web browser that can display the app](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/bug-tracking-system/codio_config_2.png)

Please refer to Codio's documentation to resolve any issues:
https://docs.codio.com/common/develop/ide/editing/preview.html

### Windows and macOS

1. Download and install Docker: https://www.docker.com/products/docker-desktop/

2. Clone the repository:

```
$ git clone https://github.com/tkachikoti/medical_practice_management_system
```

3. Change directory:

```
$ cd medical_practice_management_system
```

4. Run the app:

```
$ flask init-db
$ docker-compose up
```

5. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a browser.

## Testing the app

1. After following the relevant installation process, tests are executed from the root directory by entering:

```
$ pytest
```

### Test logs

```
========================================================================================= test session starts ==========================================================================================
platform win32 -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0 --
cachedir: .pytest_cache
rootdir: code\medical_practice_management_system
collected 27 items

tests/test_mpms_packages_address.py::AddressClassTestCase::test_address_line_2_attribute_with_data PASSED                                                                                         [  3%] 
tests/test_mpms_packages_address.py::AddressClassTestCase::test_address_line_2_attribute_without_data PASSED                                                                                      [  7%] 
tests/test_mpms_packages_address.py::AddressClassTestCase::test_county_attribute PASSED                                                                                                           [ 11%] 
tests/test_mpms_packages_healthcare_services.py::PrescriptionClassTestCase::test_address_line_2_attribute_with_data PASSED                                                                        [ 14%] 
tests/test_mpms_packages_healthcare_services.py::PrescriptionClassTestCase::test_prescription_type_attribute_with_data PASSED                                                                     [ 18%] 
tests/test_mpms_packages_healthcare_services.py::AppointmentClassTestCase::test_appointment_id_attribute_with_data PASSED                                                                         [ 22%] 
tests/test_mpms_packages_healthcare_services.py::AppointmentClassTestCase::test_postcode_attribute_with_data PASSED                                                                               [ 25%] 
tests/test_mpms_packages_healthcare_services.py::AppointmentScheduleClassTestCase::test_add_appointment_method_with_data PASSED                                                                   [ 29%]
tests/test_mpms_packages_healthcare_services.py::AppointmentScheduleClassTestCase::test_cancel_appointment_method_with_data PASSED                                                                [ 33%] 
tests/test_mpms_packages_healthcare_services.py::AppointmentScheduleClassTestCase::test_employee_name_attribute_with_data PASSED                                                                  [ 37%] 
tests/test_mpms_packages_healthcare_services.py::AppointmentScheduleClassTestCase::test_find_next_available_appointment_method_with_data PASSED                                                   [ 40%]
tests/test_mpms_packages_users.py::HealthcareProfessionalClassTestCase::test_consultation_method PASSED                                                                                           [ 44%] 
tests/test_mpms_packages_users.py::HealthcareProfessionalClassTestCase::test_employee_id_attribute PASSED                                                                                         [ 48%] 
tests/test_mpms_packages_users.py::HealthcareProfessionalClassTestCase::test_name_attribute PASSED                                                                                                [ 51%] 
tests/test_mpms_packages_users.py::DoctorClassTestCase::test_employee_id_attribute PASSED                                                                                                         [ 55%]
tests/test_mpms_packages_users.py::DoctorClassTestCase::test_issue_prescription_method PASSED                                                                                                     [ 59%] 
tests/test_mpms_packages_users.py::DoctorClassTestCase::test_name_attribute PASSED                                                                                                                [ 62%] 
tests/test_mpms_packages_users.py::NurseClassTestCase::test_employee_id_attribute PASSED                                                                                                          [ 66%] 
tests/test_mpms_packages_users.py::NurseClassTestCase::test_name_attribute PASSED                                                                                                                 [ 70%]
tests/test_mpms_packages_users.py::ReceptionistClassTestCase::test_cancel_appointment_method PASSED                                                                                               [ 74%] 
tests/test_mpms_packages_users.py::ReceptionistClassTestCase::test_employee_id_attribute PASSED                                                                                                   [ 77%] 
tests/test_mpms_packages_users.py::ReceptionistClassTestCase::test_make_appointment_method PASSED                                                                                                 [ 81%] 
tests/test_mpms_packages_users.py::ReceptionistClassTestCase::test_name_attribute PASSED                                                                                                          [ 85%]
tests/test_mpms_packages_users.py::PatientClassTestCase::test_address_postcode_attribute PASSED                                                                                                   [ 88%] 
tests/test_mpms_packages_users.py::PatientClassTestCase::test_name_attribute PASSED                                                                                                               [ 92%] 
tests/test_mpms_packages_users.py::PatientClassTestCase::test_request_appointment_method PASSED                                                                                                   [ 96%] 
tests/test_mpms_packages_users.py::PatientClassTestCase::test_request_repeat_prescription_method PASSED                                                                                           [100%]

========================================================================================== 27 passed in 0.35s ========================================================================================== 
```

## References

Heath, C., Luff, P. and Svensson, .M.S. (2003), Technology and medical practice. Sociology of Health & Illness, 25: 75-96. https://doi.org/10.1111/1467-9566.00341