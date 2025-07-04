# Expense Tracker API

A REST API for tracking expenses and income with user authentication, built using Django and Django REST Framework. The API supports user registration, login with JWT authentication, and CRUD operations for expense/income records with automatic tax calculations. Regular users can manage only their own records, while superusers can access all records. The API includes paginated responses and comprehensive tests.

# Project Overview

- User authentication with JWT tokens.
- Expense/income tracking with flat and percentage tax calculations.
- Role-based access control (regular users vs. superusers).
- Paginated API responses.
- Full CRUD operations for expense/income records.
- Comprehensive test covering authentication, CRUD, business logic, and permissions.
- Technologies**: Django, Django REST Framework, Django REST Framework SimpleJWT, Docker.


# Setup Instructions

# Prerequisites

- Python: 3.8 or higher
- Docker: Optional.
- Git: To clone the repository

# Local Setup

### 1. Clone the Repository:

```bash
git clone https://github.com/AbhinavPWN/expenseTracker.git
cd expenseTracker
```

### 2. Create and Activate a Virtual Environment:

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```


### 4. Apply Database Migrations:
```bash
python manage.py migrate
```

### 5. Create a Superuser (for testing):
```bash
python manage.py createsuperuser
```
`Example: Username: wrongdoer, Password: wrongdoer@1216`

### 6. Start the Development Server:
```bash
python manage.py runserver
```


### 7. Access the API:
```bash
Open http://localhost:8000/
```

## Docker Setup

### 1. Clone the Repository:
```bash
git clone https://github.com/AbhinavPWN/expenseTracker.git
cd expenseTracker
```


### 2. Build and Run with Docker Compose:
```bash
docker-compose up --build
```


### 3. Access the API:
```bash
Open http://localhost:8000/
```


### 4. Stop the Container:
```bash
docker-compose down
```

# API Endpoints


### Authentication Endpoints:

- `POST /api/auth/register/` : Register a new user.
- `POST /api/auth/login/` : Log in and obtain JWT tokens.
- `POST /api/auth/refresh/` : Refresh JWT token.

### Expense/Income Endpoints:

- `GET /api/expenses/` : List user's records (paginated).
- `POST /api/expenses/` : Create a new record.
- `GET /api/expenses/<id>/` : Retrieve a specific record.
- `PUT /api/expenses/<id>/` : Update a specific record.
- `DELETE /api/expenses/<id>/` : Delete a specific record.

# Testing

## 1. Manual Testing:
- Conducted using Postman with the "ExpenseTracker" collection. 
[Open Postman Collection](https://web.postman.co/workspace/My-Workspace~500fa23b-3c8b-4eff-8415-2e963524985d/collection/25457023-42526298-612a-4712-9b2d-9d44fd74e6e4?action=share&source=copy-link&creator=25457023)  

## 2. Automatic Testing:
### Python testing
```bash
python manage.py test
```
### Docker testing
```bash
docker-compose exec web python manage.py test
```