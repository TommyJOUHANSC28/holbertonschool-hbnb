# HBnb Part 2: Implementation of Business Logic and API Endpoints
## By Tommy JOUHANS and James ROUSSEL

## Task 0: Project Setup & Initialization

## Overview

This task focuses on setting up the foundational structure of the HBnB application using a modular and scalable architecture.

The goal is to prepare the project for future implementation by:

- Creating a clean project structure
- Implementing a layered architecture
- Setting up Flask with flask-restx
- Implementing an in-memory repository
- Preparing the Facade pattern for communication between layers

At this stage, no full business logic or API endpoints are implemented yet. The objective is to ensure that the project is correctly structured and ready for development.

---

# Architecture Overview

The project follows a **3-layer architecture**:


### 1️/ Presentation Layer
- Built using Flask and flask-restx
- Handles HTTP requests and responses
- Communicates only with the Facade layer

### 2️/ Business Logic Layer
- Contains domain models (User, Place, Review, Amenity)
- Implements business rules and validation
- Uses the Facade pattern to centralize logic

### 3️/ Persistence Layer
- Implements a generic repository interface
- Uses an in-memory repository for storage
- Designed to be replaced later by a database (SQLAlchemy in Part 3)



#  Components Description

## app/__init__.py
Creates the Flask application using the **App Factory Pattern** and initializes the REST API.

## api/v1/
Will contain the REST API endpoints (to be implemented in later tasks).

## models/
Will contain the business entities:
- User
- Place
- Review
- Amenity

## services/facade.py
Implements the **Facade Pattern**.

This layer:
- Acts as an intermediary between Presentation and Persistence layers
- Prevents direct repository access from the API
- Centralizes business logic

## persistence/repository.py

Defines:

- `Repository` (abstract base class)
- `InMemoryRepository` (concrete implementation)

Responsible for:
- Adding objects
- Retrieving objects
- Updating objects
- Deleting objects

The in-memory repository stores data in a Python dictionary.

---

#  Design Patterns Used

###  Facade Pattern
Provides a simplified interface between layers.

###  Repository Pattern
Abstracts data storage to allow future database replacement.

###  App Factory Pattern
Enables scalable Flask configuration and easier testing.

---

#  Installation & Setup

## 1️/ Clone the repository

bash
git clone <repository_url>
cd hbnb

## 2️/ Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

## 3️/ Install dependencies
pip install -r requirements.txt


Dependencies:

flask

flask-restx

▶ Running the Application
python run.py


If correctly configured, Flask should start successfully.

Swagger documentation will be available at:

http://127.0.0.1:5000/api/v1/


(Note: API endpoints will be implemented in later tasks.)

Objectives Achieved in Task 0

Modular project structure created

Flask application initialized

In-memory repository implemented

Facade pattern prepared

Application ready for future development

# Next Steps

In upcoming tasks, we will:

Implement business logic inside models

Complete facade methods

Create RESTful CRUD endpoints

Add validation logic

Implement data serialization

Introduce authentication (JWT) in a later phase

# Learning Goals

This task helps reinforce:

Modular application design

Separation of concerns

Clean API architecture

Design patterns in Python

Scalable Flask project organization

## Important Note

Authentication and role-based access control will be implemented in a later part of the project.

## Task 1: Core Business Logic Classes

##  Overview

Part 2 of the HBnB project focuses on implementing the core business logic and REST API endpoints based on the architecture designed in Part 1.

This phase includes:

- Implementation of domain models (User, Place, Review, Amenity)
- Strict attribute validation
- Entity relationships management
- Facade pattern implementation
- In-memory persistence using Repository pattern
- Full CRUD REST API using Flask and flask-restx
- Advanced serialization with nested objects
- Unit testing of business logic

Authentication (JWT) and database integration will be implemented in Part 3.

---

#  Architecture

The project follows a clean 3-layer architecture:

Presentation Layer → Business Logic Layer → Persistence Layer
(API) (Facade + Models) (Repository)

yaml
Copier le code

---

## 1️/ Presentation Layer (`app/api/`)

Built using:

- Flask
- flask-restx

Responsibilities:

- Handle HTTP requests
- Validate request payloads
- Call the Facade
- Return structured JSON responses

All API routes are versioned under:

/api/v1/

arduino
Copier le code

Swagger documentation is available at:

http://127.0.0.1:5000/api/v1/

yaml
Copier le code

---

## 2️/ Business Logic Layer (`app/models/` + `app/services/`)

### 🔹 BaseModel

All entities inherit from `BaseModel`.

Common attributes:

- `id` (UUID string)
- `created_at`
- `updated_at`

Common methods:

- `save()`
- `update(data)`
- `to_dict()`

UUIDs are used instead of numeric IDs for:

- Global uniqueness
- Security (non-sequential IDs)
- Scalability in distributed systems

---

###  User

Attributes:

- `first_name` (required, max 50 chars)
- `last_name` (required, max 50 chars)
- `email` (required, unique, valid format)
- `password` (required)
- `is_admin` (default: False)

Validations:

- Email format validation (regex)
- Length constraints
- Email uniqueness enforced in Facade

Relationships:

- A user can own multiple places
- A user can write multiple reviews

---

###  Place

Attributes:

- `title` (required, max 100 chars)
- `description` (optional)
- `price` (positive float)
- `latitude` (-90 to 90)
- `longitude` (-180 to 180)
- `owner` (User instance)

Relationships:

- One-to-many: Place → Reviews
- Many-to-many: Place → Amenities

Validations:

- Price must be positive
- Coordinates must be within valid geographic ranges
- Owner must exist

---

###  Review

Attributes:

- `text` (required)
- `rating` (integer 1–5)
- `user` (User instance)
- `place` (Place instance)

Validations:

- Rating must be between 1 and 5
- Place and User must exist

---

###  Amenity

Attributes:

- `name` (required, max 50 chars)

---

# Facade Pattern (`app/services/facade.py`)

The `HBnBFacade` class centralizes business logic and acts as the single entry point between the API and the persistence layer.

Responsibilities:

- Validate relationships
- Ensure entity existence
- Enforce email uniqueness
- Manage object creation and updates
- Coordinate repository operations

Example:


facade.create_user(data)

facade.create_place(data)


Benefits:

Loose coupling

Clean API layer

Easy maintainability

### Future database integration without API changes


Persistence Layer (app/persistence/)

Implements the Repository pattern.

Repository Interface

Defines:

add()

get()

get_all()

update()

delete()

get_by_attribute()

InMemoryRepository


### Stores objects in Python dictionaries:

{

    "uuid1": object1,

    "uuid2": object2
}

Characteristics:

Fast access

No database required

Data lost when application stops

Designed to be replaced in Part 3

REST API – Full CRUD

CRUD operations implemented for:

Users

Places

Reviews

Amenities

Example:

POST    /users

GET     /users

GET     /users/<id>

PUT     /users/<id>

DELETE  /users/<id>


Users:

POST    /users

GET     /users

GET     /users/<id>

PUT     /users/<id>

DELETE  /users/<id>


Similar endpoints exist for Places, Reviews, and Amenities.

### Advanced Serialization

Nested relationships are included in responses.

Example:

GET /places/<id>


Response includes:

Owner details (first_name, last_name)

Amenities list

Reviews list

Example JSON:

{

  "id": "...",

  "title": "Cozy Apartment",

  "price": 100,

  "owner": {

    "id": "...",


    "first_name": "John",

    "last_name": "Doe"
  
},


  "amenities": [

    {"name": "Wi-Fi"},

    {"name": "Parking"}

  ],

  "reviews": [

    {


      "text": "Great stay!",

      "rating": 5

    }
 ]

}

### Unit Testing

Basic unit tests verify:

Object creation

Validation rules

Relationship integrity

Update functionality

Tests cover:

User creation

Place ownership

Review linking

Amenity creation

Example test:

def test_user_creation():

    user = User("John","Doe", "john@example.com", "1234")
    assert user.first_name == "John"
    assert user.is_admin is False


## Task 2 : User Endpoints Implementation

## Overview

This section implements the main CRUD operations for user management in the HBnB application.

Implemented endpoints:

- POST /api/v1/users/
- GET /api/v1/users/
- GET /api/v1/users/<user_id>
- PUT /api/v1/users/<user_id>

The DELETE operation is not implemented in this phase.

---

## Business Logic Integration

All user operations are handled through the `HBnBFacade`.

The API layer does not directly interact with the repository.

Flow:

Client → API → Facade → Repository → Model

---

## Password Security

User passwords are never included in API responses.

The `to_dict()` method removes the password field before returning JSON data.

---

## Endpoint Details

### Create User

POST /api/v1/users/

Response:
- 201 Created
- 400 Bad Request (email already exists or invalid input)

---

### Retrieve User by ID

GET /api/v1/users/<user_id>

Response:
- 200 OK
- 404 Not Found

---

### Retrieve All Users

GET /api/v1/users/

Response:
- 200 OK

Returns a list of users (without passwords).

---

### Update User

PUT /api/v1/users/<user_id>

Response:
- 200 OK
- 404 Not Found
- 400 Bad Request

---

## Testing

Endpoints can be tested using:

- Swagger UI
- Postman
- cURL

Example:


curl -X POST http://localhost:5000/api/v1/users/ \

-H "Content-Type: application/json" \

-d '{"first_name":"John","last_name":"Doe","email":"john@example.com","password":"1234"}'

Status Codes Summary

201 → User successfully created

200 → Successful retrieval or update

400 → Invalid input or duplicate email

404 → User not found


# Task 3 : Amenity Endpoints Implementation

## Overview

This section implements the CRUD operations for Amenity management in the HBnB application.

Implemented endpoints:

- POST /api/v1/amenities/
- GET /api/v1/amenities/
- GET /api/v1/amenities/<amenity_id>
- PUT /api/v1/amenities/<amenity_id>

The DELETE operation is not implemented in this phase.

---

## Business Logic Integration

All Amenity operations are handled via the `HBnBFacade`.

Flow:

Client → API → Facade → Repository → Amenity Model

The API layer never directly accesses the repository.

---

## Endpoint Details

### Create Amenity

POST /api/v1/amenities/

Response:
- 201 Created
- 400 Bad Request (invalid input)

---

### Retrieve All Amenities

GET /api/v1/amenities/

Response:
- 200 OK

Returns a list of all amenities.

---

### Retrieve Amenity by ID

GET /api/v1/amenities/<amenity_id>

Response:
- 200 OK
- 404 Not Found

---

### Update Amenity

PUT /api/v1/amenities/<amenity_id>

Response:
- 200 OK
- 404 Not Found
- 400 Bad Request

---

## Example

Create amenity:


curl -X POST http://localhost:5000/api/v1/amenities/ \

-H "Content-Type: application/json" \

-d '{"name":"Wi-Fi"}'

# Task 4 : Place Endpoints Implementation

## Overview

This section implements CRUD operations for Place management.

Implemented endpoints:

- POST /api/v1/places/
- GET /api/v1/places/
- GET /api/v1/places/<place_id>
- PUT /api/v1/places/<place_id>

DELETE is not implemented in this phase.

---

## Relationships Handling

Place is linked to:

- Owner (User)
- Amenities (many-to-many)

Validations ensure:

- Owner exists
- Amenities exist
- Price ≥ 0
- Latitude between -90 and 90
- Longitude between -180 and 180

---

## Advanced Serialization

Place responses include:

- Owner details
- List of amenities

Example response:

{

  "id": "...",

  "title": "Cozy Apartment",

  "price": 100,

  "owner": {

    "first_name": "John",

    "last_name": "Doe"

  },
  "amenities": [

    {"name": "Wi-Fi"}

  ]

}

---

## Status Codes

- 201 → Place created
- 200 → Success
- 400 → Invalid input
- 404 → Place not found



# Authors

- **James Roussel**
- **Tommy Jouhans**

---