from flask import Flask, jsonify, request, abort
from functools import wraps
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "dbroot",  # Replace with your MySQL username
    "password": "root",  # Replace with your MySQL password
    "database": "py_sample",
}


# Middleware to check if the user is an admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Assuming the role is passed in the headers
        role = request.headers.get("Role")
        if role != "admin":
            abort(403, description="Admin role required")
        return f(*args, **kwargs)

    return decorated_function


# Helper function to get a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)


# Create an employee
@app.route("/employee", methods=["POST"])
@admin_required
def create_employee():
    data = request.get_json()
    name = data.get("name")
    position = data.get("position")

    if not name or not position:
        abort(400, description="Name and position are required")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, position) VALUES (%s, %s)", (name, position)
    )
    conn.commit()
    employee_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({"id": employee_id, "name": name, "position": position}), 201


# Read all employees
@app.route("/employees", methods=["GET"])
def read_employees():
    message = ""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    if employees:
        message = "Employees found successsfully"
    else:
        message = "Employee not found"
    cursor.close()
    conn.close()

    return jsonify({"message": message, "data": employees})


# Read a single employee by ID
@app.route("/employee/<int:employee_id>", methods=["GET"])
def read_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()

    if employee is None:
        abort(404, description="Employee not found")

    return jsonify(employee)


# Update an employee by ID
@app.route("/employee/<int:employee_id>", methods=["PUT"])
@admin_required
def update_employee(employee_id):
    data = request.get_json()
    name = data.get("name")
    position = data.get("position")

    if not name or not position:
        abort(400, description="Name and position are required")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET name = %s, position = %s WHERE id = %s",
        (name, position, employee_id),
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"id": employee_id, "name": name, "position": position})


# Delete an employee by ID
@app.route("/employee/<int:employee_id>", methods=["DELETE"])
@admin_required
def delete_employee(employee_id):
    message = ""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
    employee = cursor.fetchone()
    if employee:
        cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
        message = "Employee deleted"
    else:
        message = "Employee not found"
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": message})


# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404


# Error handler for 403
@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": str(error)}), 403


# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(debug=True)
