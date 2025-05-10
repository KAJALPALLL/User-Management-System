* * USER MANAGEMENT API 

 This project is a backend REST API assignment for managing user data using Django and REST Framework. 
 It supports full CRUD functionality, filtering, pagination, and sorting as per assignment requirements.

* * Features

1. Create, Read, Update, Delete Users
2. Search users by name (case-insensitive substring match)
3. Sort users by any field (ascending/descending)
4. Pagination with page and limit query parameters

* * Unit tests for all API endpoints

* * Tech Stack

1. Python 3
2. Django 5+
3. Django REST Framework
4. DBSQLite3 (default)

* * Setup Instructions

1. Clone the repo

git clone https://github.com/KAJALPALLL/User-Management-System.git
cd user-api-django

2. Create virtual environment

python -m venv env
source env/bin/activate for Linux  # or .\env\Scripts\activate for Windows

3. Install dependencies

pip install -r requirements.txt

4. Apply migrations

python manage.py makemigrations
python manage.py migrate

5. Run the server

python manage.py runserver 0.0.0.0:8000

6. Access API

http://127.0.0.1:8000/api/users

* * API Endpoints

* List users
GET (method) -  /api/users
Query Params: page, limit, name, sort

* Get user by ID
GET /api/users/<id>

* Create a user
POST /api/users

* Update user by ID
PUT /api/users/<id>

* Delete user by ID
DELETE /api/users/<id>


* * Running Tests
python manage.py test users
