import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.db import get_db

from app.mpms_packages.healthcare_services import AppointmentSchedule
from app.mpms_packages.system_users import Patient
from app.mpms_packages.system_users import Doctor
from app.mpms_packages.system_users import HealthcareProfessional

bp = Blueprint('services', __name__, url_prefix='/services')

@bp.route("/", methods=['GET'])
def index():
    """Render the index page of the services section of the application.
    """
    db = get_db()

    patient_table_data = db.execute(
        'SELECT * FROM patient'
    ).fetchall()

    return render_template(
        'services/index.html.jinja',
        page_title='Services',
        patient_table_data=patient_table_data)

@bp.route("/consultation", methods=['GET', 'POST'])
def consultation():
    """Create a consultation."""
    return render_template(
            'services/consultation.html.jinja',
            page_title='Consultation')
