# Flask CRUD Operations with MySQL, JWT, and MVC Architecture 🛠️

This repository demonstrates a simple CRUD (Create, Read, Update, Delete) operation implementation for managing employees, with integration to MySQL and JWT-based authentication. The project follows the **MVC** (Model-View-Controller) architecture for clean separation of concerns.

## Features ✨:

- **MySQL Integration**: This project connects to a MySQL database to store employee data. 🗄️
- **MVC Structure**: The application follows the MVC design pattern for better code organization. 🏗️
- **JWT Authentication**: JSON Web Token (JWT) is used for securing API endpoints and authenticating users. 🔑
- **CRUD Operations**: The system supports basic CRUD operations for employee management, with an **Admin role** granting full access. 📝

## Requirements 📋:

Before running the project, make sure you have the following installed:

- **Python 3.x** 🐍
- **MySQL** Database 💾
- **Postman** (optional, for testing APIs) 🧪

## Getting Started 🚀

### 1. Clone the Repository:

```bash
git clone https://github.com/prashant1879/flask-crud-with-mysql-and-jwt.git
cd flask-crud-with-mysql-and-jwt
```

### 2. Install Required Dependencies:

Make sure you have a `requirements.txt` file in the repository. You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

This will install the necessary Python libraries such as Flask, Flask-JWT-Extended, Flask-MySQLdb, etc. 📦

### 3. Set Up the Database:

- Create a MySQL database (e.g., `employee_db`). 🏢
- Import the database schema to create the necessary tables. 🗂️
- Update the `db.py` or environment variables with your database credentials. 🔧

### 4. Run the Application:

You can start the Flask development server with:

```bash
python run.py
```

🚨 **Note**: Ensure your database is set up correctly before running the server.

## Folder Structure 📁

```
/project-root
├── /app
│   ├── /models         # Database models 📊
│   ├── /middleware     # middleware folder 🔒
│   ├── /controllers    # CRUD operation logic ⚙️
│   ├── /views          # Views for rendering templates (if applicable) 👀
│   └── /utils          # Utility functions (e.g., JWT handling) 🔧
├── /migrations         # Database migration scripts 🛠️
├── .env                # ENV file 🌱
├── .gitignore          # GIT file 🔍
├── requirements.txt    # Python dependencies 📜
├── Dockerfile          # Docker setup file 🐳
├── docker-compose.yml  # Docker setup file 🛠️
├── remove_cache.sh     # remove py cache in linux 🧹
└── run.py              # Main application entry point ▶️
```

## Improvements and Future Features 🚧:

- Add unit tests for endpoints. 🧪
- Implement role-based access control more extensively. 🔐
- Support for employee search and filtering. 🔍
- Docker deployment 🐳

## License 📜

This project is licensed under the MIT License.

---

### Want to Learn More? 🤓

If you're interested in diving deeper into Node.js, DevOps, and other tech topics, follow me on Medium for more insightful articles and guides! ✨

👉 [Follow me on Medium!](https://prashant1879.medium.com/) 📚

Stay tuned and keep coding! 👨‍💻👩‍💻
