from flask import jsonify, request, abort
from app.models.employee import Employee
from app.middleware.jwt_middleware import admin_required

# def admin_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         role = request.headers.get("Role")
#         if role != "admin":
#             abort(403, description="Admin role required")
#         return f(*args, **kwargs)
#     return decorated_function

@admin_required
def create_employee():
    data = request.get_json()
    name = data.get("name")
    position = data.get("position")

    if not name or not position:
        abort(400, description="Name and position are required")

    employee_id = Employee.create(name, position)
    return jsonify({"id": employee_id, "name": name, "position": position}), 201


def read_employees():
    employees = Employee.get_all()
    message = "Employees found successfully" if employees else "Employee not found"
    return jsonify({"message": message, "data": employees})


def read_employee(employee_id):
    employee = Employee.get_by_id(employee_id)
    if not employee:
        abort(404, description="Employee not found")
    return jsonify(employee)


def update_employee(employee_id):
    data = request.get_json()
    name = data.get("name")
    position = data.get("position")

    if not name or not position:
        abort(400, description="Name and position are required")

    Employee.update(employee_id, name, position)
    return jsonify({"id": employee_id, "name": name, "position": position})


def delete_employee(employee_id):
    employee = Employee.get_by_id(employee_id)
    if not employee:
        return jsonify({"message": "Employee not found"})
    Employee.delete(employee_id)
    return jsonify({"message": "Employee deleted"})
