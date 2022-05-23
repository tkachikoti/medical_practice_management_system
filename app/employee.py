import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.db import get_db

bp = Blueprint('employee', __name__, url_prefix='/employee')

@bp.route("/", methods=['GET'])
def index():
    """Render the index page of the application. The function also
    performs a sort operation on the data from the tickets.csv file.
    """
    db = get_db()
    employee_table_data = db.execute(
        'SELECT id, name'
        ' FROM employee'
        ' ORDER BY id ASC'
    ).fetchall()
    return render_template(
        'employee/index.html.jinja',
        page_title='Employee Table',
        employee_table_data=employee_table_data)

@bp.route("/create", methods=['GET', 'POST'])
def create():
    """Create a new employee.
    """
    print("Here we are!")
    print(request.form)
    print(request.form.get('name', False))
    if request.method == 'POST' and request.form.get('name', False):
        name = request.form.get('name', None)
        employee_id = request.form.get('employee_id', None)
        # Get the database connection
        db = get_db()
        try:
            db.execute(
                "INSERT INTO employee (name) VALUES (?)",
                [name],
            )
            db.commit()
        except db.IntegrityError:
            error = f"Employee {name} is already registered."

        # Redirect to the home page
        return redirect(url_for('employee.index'))
    return render_template(
        'employee/create.html.jinja',
        page_title='Create Employee',
        employee_data=None)

@bp.route("/update", methods=['GET', 'POST'])
def create():
    """Update employee details.
    """
    print("Here we are!")
    print(request.form)
    print(request.form.get('name', False))
    if request.method == 'POST' and request.form.get('name', False):
        name = request.form.get('name', None)
        employee_id = request.form.get('employee_id', None)
        # Get the database connection
        db = get_db()
        try:
            db.execute(
                "INSERT INTO employee (name) VALUES (?)",
                [name],
            )
            db.commit()
        except db.IntegrityError:
            error = f"Employee {name} is already registered."

        # Redirect to the home page
        return redirect(url_for('employee.index'))
    return render_template(
        'employee/create.html.jinja',
        page_title='Create Employee',
        employee_data=None)