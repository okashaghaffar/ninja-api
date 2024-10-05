# Employee Management REST API
This is a simple Employee Management REST API built using the Ninja Framework for Django. The API allows users to manage employees and departments with full CRUD functionality, including file uploads for employee resumes (CVs).

# Features
Authentication check: Routes to verify if a user is authenticated.
Employee Management: Create, read, update, and delete employee records.
Department Management: Create departments to assign employees.
File Upload: Upload employee CVs (resumes) during employee creation.
Database Models: Integrated with Django ORM to handle database operations.
# API Endpoints
# User Authentication
GET /me: Retrieve authenticated user details.
GET /me/user: Retrieve authenticated user details or return error if not signed in.
# Employee Management
POST /employees: Create a new employee with optional CV file upload.
GET /employees/{employee_id}: Retrieve details of a specific employee.
GET /employees: List all employees.
PUT /employees/{employee_id}: Update an existing employee's details.
DELETE /employees/{employee_id}: Delete an employee.
# Department Management
POST /dept: Create a new department.
# Install Package from requirements.txt
### `pip install -r requirements.txt`
# For Migrating
### `python manage.py migrate`
# Use Following Command For staring Server
### `python manage.py runserver`
