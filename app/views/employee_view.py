from flask import Blueprint, jsonify
from app.utils.db import generate_temp_token
from app.controllers.employee_controller import (
    create_employee,
    read_employees,
    read_employee,
    update_employee,
    delete_employee,
)

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employee", methods=["POST"])
def create():
    return create_employee()


@employee_bp.route("/employees", methods=["GET"])
def read_all():
    return read_employees()


@employee_bp.route("/employee/<int:employee_id>", methods=["GET"])
def read_one(employee_id):
    return read_employee(employee_id)


@employee_bp.route("/employee/<int:employee_id>", methods=["PUT"])
def update(employee_id):
    return update_employee(employee_id)


@employee_bp.route("/employee/<int:employee_id>", methods=["DELETE"])
def delete(employee_id):
    return delete_employee(employee_id)


@employee_bp.route("/generate_temp_token", methods=["GET"])
def generate_temp_token():
    print("generate_temp_token>")
    return jsonify(generate_temp_token())
