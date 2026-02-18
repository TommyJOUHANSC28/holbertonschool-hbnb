# HBnB – Modular REST API (Part 2) 
# By Tommy JOUHANS and James ROUSSEL

## Project Overview

HBnB is a modular RESTful API built with **Flask** and **flask-restx**.

This project implements a clean and scalable layered architecture including:

- Presentation Layer (API)
- Business Logic Layer (Models + Facade)
- Persistence Layer (Repository Pattern)

The application manages:

- Users
- Places
- Reviews
- Amenities

At this stage:
- Data is stored in memory
- No authentication (JWT) yet
- The architecture is prepared for future database integration

---

# Architecture Overview

The project follows a **3-layer architecture**:

Presentation Layer → Business Logic Layer → Persistence Layer

(API) (Facade + Models) (Repository)


---

## 1️/ Presentation Layer (`app/api/`)

Built with:
- Flask
- flask-restx

Responsibilities:
- Handle HTTP requests
- Validate request payload
- Call the Facade
- Return JSON responses

The API is versioned under:

/api/v1/


Example endpoints:

POST /users

GET /users

GET /users/<id>

POST /places

GET /places

POST /reviews

GET /reviews

POST /amenities

GET /amenities



The API never accesses the repository directly.  
All calls go through the Facade.

---

## 2️/ Business Logic Layer (`app/models/` + `app/services/`)

### Models (`app/models/`)

Entities:

- `BaseModel`
- `User`
- `Place`
- `Review`
- `Amenity`

Each model:
- Inherits from `BaseModel`
- Has a unique UUID
- Contains timestamps (`created_at`, `updated_at`)
- Implements `update()` and `to_dict()`

Relationships:

- A User owns multiple Places
- A User writes multiple Reviews
- A Place has multiple Reviews
- A Place includes multiple Amenities

---

### Facade (`app/services/facade.py`)

Implements the **Facade Pattern**.

Responsibilities:
- Centralize business logic
- Validate relationships
- Interact with repositories
- Prevent direct repository access from API

Example:

facade.create_user(data)
facade.create_place(data)

3️/ Persistence Layer (app/persistence/)

Implements the Repository Pattern.

Repository Interface

Defines abstract methods:

add()

get()

get_all()

update()

delete()

get_by_attribute()

InMemoryRepository

Stores objects in a dictionary:


{
   "uuid1": object1,
   "uuid2": object2
}

This layer is designed to be replaced later by a database implementation (SQLAlchemy).

Design Patterns Used
## Facade Pattern

Provides a unified interface to the business logic layer.

## Repository Pattern

## Abstracts data storage and allows easy replacement of storage implementation.

 App Factory Pattern

Used in app/__init__.py to create scalable Flask applications.

## Installation & Setup
## 1️/ Clone the repository
git clone <repository_url>
cd hbnb

## 2/Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

## 3️/ Install dependencies
pip install -r requirements.txt


Dependencies:

flask

flask-restx

▶ Running the Application
python run.py


If correctly configured, the application runs at:

http://127.0.0.1:5000/


Swagger documentation is available at:

http://127.0.0.1:5000/api/v1/

## Testing the API

You can test endpoints using:

Postman

curl

Swagger UI

Example:

curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"first_name":"John","last_name":"Doe","email":"john@example.com","password":"1234"}'

## Future Improvements

Planned next steps:

Implement JWT authentication

Add role-based access control

Replace InMemoryRepository with SQLAlchemy

Add advanced serialization

Add filtering & pagination

Write full unit tests

# Learning Objectives Achieved

This project demonstrates:

Clean architecture design

Separation of concerns

REST API development with Flask

Implementation of design patterns in Python

Modular and scalable backend structure

## Important Notes

Data is currently stored in memory.

Restarting the server resets all stored data.

Authentication will be implemented in the next phase.