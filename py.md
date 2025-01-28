Certainly! To integrate MySQL with the Flask application, we'll use the `mysql-connector-python` package to connect to the MySQL database. Below is the updated code with MySQL integration.

---

### Step 1: Install Required Packages
Install the necessary packages:

```bash
pip install Flask mysql-connector-python
```

---

### Step 2: Set Up MySQL Database
Create a MySQL database and a table for employees. For example:

```sql
CREATE DATABASE company;

USE company;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL
);
```

---

### Step 3: Update the Flask Application

Here’s the updated `app.py` with MySQL integration:

```python
from flask import Flask, jsonify, request, abort
from functools import wraps
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'database': 'company'
}

# Middleware to check if the user is an admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Assuming the role is passed in the headers
        role = request.headers.get('Role')
        if role != 'admin':
            abort(403, description="Admin role required")
        return f(*args, **kwargs)
    return decorated_function

# Helper function to get a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Create an employee
@app.route('/employee', methods=['POST'])
@admin_required
def create_employee():
    data = request.get_json()
    name = data.get('name')
    position = data.get('position')

    if not name or not position:
        abort(400, description="Name and position are required")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, position) VALUES (%s, %s)', (name, position))
    conn.commit()
    employee_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({'id': employee_id, 'name': name, 'position': position}), 201

# Read all employees
@app.route('/employees', methods=['GET'])
def read_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(employees)

# Read a single employee by ID
@app.route('/employee/<int:employee_id>', methods=['GET'])
def read_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM employees WHERE id = %s', (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()

    if employee is None:
        abort(404, description="Employee not found")

    return jsonify(employee)

# Update an employee by ID
@app.route('/employee/<int:employee_id>', methods=['PUT'])
@admin_required
def update_employee(employee_id):
    data = request.get_json()
    name = data.get('name')
    position = data.get('position')

    if not name or not position:
        abort(400, description="Name and position are required")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE employees SET name = %s, position = %s WHERE id = %s', (name, position, employee_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'id': employee_id, 'name': name, 'position': position})

# Delete an employee by ID
@app.route('/employee/<int:employee_id>', methods=['DELETE'])
@admin_required
def delete_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = %s', (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Employee deleted'})

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for 403
@app.errorhandler(403)
def forbidden(error):
    return jsonify({'error': str(error)}), 403

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Step 4: Run the Application

Run the Flask application:

```bash
python app.py
```

---

### Step 5: Test the CRUD Operations

You can use `curl`, Postman, or any HTTP client to test the endpoints.

#### Create an Employee (POST)
```bash
curl -X POST -H "Content-Type: application/json" -H "Role: admin" -d '{"name": "John Doe", "position": "Software Engineer"}' http://127.0.0.1:5000/employee
```

#### Read All Employees (GET)
```bash
curl -X GET http://127.0.0.1:5000/employees
```

#### Read a Single Employee by ID (GET)
```bash
curl -X GET http://127.0.0.1:5000/employee/1
```

#### Update an Employee by ID (PUT)
```bash
curl -X PUT -H "Content-Type: application/json" -H "Role: admin" -d '{"name": "Jane Doe", "position": "Senior Software Engineer"}' http://127.0.0.1:5000/employee/1
```

#### Delete an Employee by ID (DELETE)
```bash
curl -X DELETE -H "Role: admin" http://127.0.0.1:5000/employee/1
```

---

### Explanation of Changes

1. **MySQL Connection**:
   - The `get_db_connection()` function establishes a connection to the MySQL database using the `mysql.connector` package.
   - The connection is closed after each operation to avoid connection leaks.

2. **Database Queries**:
   - SQL queries are used to perform CRUD operations on the `employees` table.
   - For example:
     - `INSERT INTO employees` for creating an employee.
     - `SELECT * FROM employees` for reading employees.
     - `UPDATE employees` for updating an employee.
     - `DELETE FROM employees` for deleting an employee.

3. **Error Handling**:
   - Added a `400 Bad Request` error handler for invalid input.
   - Ensured proper error messages for `404 Not Found` and `403 Forbidden`.

4. **Middleware**:
   - The `admin_required` middleware ensures that only users with the `admin` role can perform certain operations (e.g., create, update, delete).

---

### Notes

- Replace the `db_config` values with your MySQL credentials.
- In a production environment, use environment variables or a configuration file to store sensitive database credentials.
- You can enhance this application by adding authentication (e.g., JWT) and more advanced error handling.