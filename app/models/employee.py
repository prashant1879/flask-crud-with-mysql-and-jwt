from app.utils.db import get_db_connection

class Employee:
    @staticmethod
    def create(name, position):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", (name, position))
        conn.commit()
        employee_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return employee_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees

    @staticmethod
    def get_by_id(employee_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
        employee = cursor.fetchone()
        cursor.close()
        conn.close()
        return employee

    @staticmethod
    def update(employee_id, name, position):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE employees SET name = %s, position = %s WHERE id = %s", (name, position, employee_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(employee_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
        conn.commit()
        cursor.close()
        conn.close()