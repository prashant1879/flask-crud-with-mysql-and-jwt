from flask import jsonify, request
from flask_jwt_extended import create_access_token
from app.models.employee import Employee
from app.middleware.jwt_middleware import admin_required


@admin_required
def create_employee():
    data = request.get_json()
    name = data.get("name")
    position = data.get("position")

    if not name or not position:
        return jsonify({"message": "Name and position are required"}), 400

    employee_id = Employee.create(name, position)
    return jsonify({"id": employee_id, "name": name, "position": position}), 201


@admin_required
def read_employees():
    employees = Employee.get_all()
    message = "Employees found successfully" if employees else "Employee not found"
    return jsonify({"message": message, "data": employees}), 200


@admin_required
def read_employee(employee_id):
    employee = Employee.get_by_id(employee_id)
    if not employee:
        return jsonify({"message": "Employee not found"}), 400

    return jsonify(employee)


@admin_required
def update_employee(employee_id):
    data = request.get_json()
    name = data.get("name")
    position = data.get("position")

    if not name or not position:
        return jsonify({"message": "Name and position are required"}), 400

    Employee.update(employee_id, name, position)
    return jsonify({"id": employee_id, "name": name, "position": position}), 200


@admin_required
def delete_employee(employee_id):
    employee = Employee.get_by_id(employee_id)
    if not employee:
        return jsonify({"message": "Employee not found"})
    Employee.delete(employee_id)
    return jsonify({"message": "Employee deleted"})


def generate_temp_token():
    # Example: Generate a token for a user with a specific role
    user_id = "1"  # Replace with actual user ID
    role = "admin"  # Replace with actual role

    # Create a JWT token with additional claims (e.g., role)
    access_token = create_access_token(
        identity=user_id, additional_claims={"role": role, "area": "Ahmedabad"}
    )
    return jsonify({"access_token": access_token}), 200
