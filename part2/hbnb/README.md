# HBnb Part 2: Implementation of Business Logic and API Endpoints
## Business Logic & REST API Implementation
### Authors: Tommy Jouhans & James Roussel
---

## Project Objective

This phase implements the complete Business Logic Layer and REST API Layer of the HBnB application.

The goal is to build:

- A modular scalable architecture
- Strict data validation
- Full RESTful API
- In-memory persistence
- Relationship management between entities
- Unit and manual testing
- Swagger documentation


---

## Project Structure

![HBNB tree](https://github.com/TommyJOUHANSC28/holbertonschool-hbnb/blob/main/part2/images/hbnb-tree.png)

---


## Architecture Overview

The project follows a strict 3-layer architecture:

![HBNB UML Task 0](https://github.com/TommyJOUHANSC28/holbertonschool-hbnb/blob/main/part2/images/task0.png)

---

#  Installation & Setup

## 1️/ Clone the repository

Bash:
```shell
- git clone <repository_url>
- cd part2
```

## 2️/ Create a virtual environment (recommended)
```shell
- python3 -m venv venv
- source venv/bin/activate
```

## 3️/ Install dependencies
```shell
- pip install -r requirements.txt
```

Dependencies:

- flask
- flask-restx

▶ Running the Application
```shell
- python -m hbnb.run
```

If correctly configured, Flask should start successfully.

Swagger documentation will be available at:

http://127.0.0.1:5000/api/v1/

---

## TASK 0 – Project Initialization

### Objective

Set up scalable architecture using:

Flask App Factory Pattern

Repository Pattern

Facade Pattern

In-memory storage

### Key Files

app/init.py

Registers namespaces:

- api.add_namespace(users_ns, path="/api/v1/users")
- api.add_namespace(places_ns, path="/api/v1/places")
- api.add_namespace(amenities_ns, path="/api/v1/amenities")
- api.add_namespace(reviews_ns, path="/api/v1/reviews")

### persistence/repository.py

```python
class InMemoryRepository:
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update(data)
        return obj

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]

```
---
## TASK 1 – Core Business Models

###  BaseModel

Provides:

- UUID id
- created_at
- updated_at
- update() method
```python
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
```

### User Model

Validations:

- first_name required
- last_name required
- valid email format

```python
if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
    raise ValueError("Invalid email format")
```

### Place Model

Validations:
- price ≥ 0
- latitude ∈ [-90, 90]
- longitude ∈ [-180, 180]

Supports both:

- owner object (tests)
- owner_id (API)

### Review Model

Supports both:

- user + place objects (tests)
- user_id + place_id (API)

Rating validation:
```python
if not (1 <= rating <= 5):
    raise ValueError("Rating must be between 1 and 5")
```

### Amenity Model
```python
class Amenity(BaseModel):
    def __init__(self, name, description=None):
        if not name:
            raise ValueError("Amenity name is required")
        super().__init__()
```
---
### TASK 2 – User Endpoints
### POST /api/v1/users
- Creates a new user
- Validates input data
- Returns created user with 201 status
- Error handling for missing fields and invalid email

```shell
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'
```

### GET /api/v1/users/
- Retrieves all users
- Returns list of users with 200 status
- Supports pagination (optional)
- Error handling for empty database
- 
```shell
curl http://127.0.0.1:5000/api/v1/users/
```
### PUT /api/v1/users/<user_id>
- Updates user information
- Validates input data
- Returns updated user with 200 status
- Error handling for invalid user_id and missing fields

```shell
curl -X PUT http://127.0.0.1:5000/api/v1/users/<USER_ID> \
-H "Content-Type: application/json" \
-d '{"first_name":"Jane","Doe":"Smith","email":"jane.doe@example.com"}'
```


Validation errors return:

- 400 Bad Request
- 404 Not Found

---

### TASK 3 – Amenity Endpoints

### POST /api/v1/amenities
- Creates a new amenity
- Validates input data
- Returns created amenity with 201 status
- Error handling for missing fields

```shell
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \
-H "Content-Type: application/json" \
-d '{"name":"Wi-Fi"}'
```

### GET /api/v1/amenities/
- Retrieves all amenities
- Returns list of amenities with 200 status
- Supports pagination (optional)
- Error handling for empty database

```shell
curl http://127.0.0.1:5000/api/v1/amenities/
```

### PUT /api/v1/amenities/<amenity_id>
- Updates amenity information
- Validates input data
- Returns updated amenity with 200 status
- Error handling for invalid amenity_id and missing fields

```shell
curl -X PUT http://127.0.0.1:5000/api/v1/amenities/<AMENITY_ID> \
-H "Content-Type: application/json" \
-d '{"name": "Air Conditioning"}'
```
---


### TASK 4 – Place Endpoints

### POST /api/v1/places
- Creates a new place
- Validates input data
- Returns created place with 201 status
- Error handling for missing fields and invalid data
- Supports both owner_id and owner object for testing
- Validation errors return:
- 400 Bad Request
- 404 Not Found

```shell
curl -X POST http://127.0.0.1:5000/api/v1/places/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Cozy Apartment",
  "description": "A nice place to stay",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id":"<USER_ID>"
}'
```

### GET /api/v1/places/
- Retrieves all places
- Returns list of places with 200 status


```shell
curl http://127.0.0.1:5000/api/v1/places/

```

### PUT /api/v1/places/<place_id>
- Updates place information
- Validates input data
- Returns updated place with 200 status
- Error handling for invalid place_id and missing fields
- Supports both owner_id and owner object for testing
- Validation errors return:
- 400 Bad Request
- 404 Not Found

```shell
curl -X PUT http://127.0.0.1:5000/api/v1/places/<PLACE_ID> \
-H "Content-Type: application/json" \
-d '{
  "title": "Luxury Condo",
  "description": "An upscale place to stay",
  "price": 200.0
}'
```

### POST Amenity for Place
```shell
 curl -X POST http://127.0.0.1:5000/api/v1/places/<PLACE_ID>/amenities/<amenities_id>
```



### Validations

- Owner must exist
- Coordinates valid
- Price ≥ 0

---

## TASK 5 – Review Endpoints

### Create Review
```shell
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
-H "Content-Type: application/json" \
-d '{
"text":"Great place to stay",
"rating":5,
"user_id":"<USER_ID>",
"place_id":"<PLACE_ID>"
}'
```

### GET Review
```shell
curl http://127.0.0.1:5000/api/v1/review/
```

### PUT Review
```shell
curl -X PUT http://127.0.0.1:5000/api/v1/reviews/<REVIEW_ID> \
-H "Content-Type: application/json" \
-d '{
"text": "Amazing stay!",
"rating": 4
}'
```

### Delete Review

```shell
curl -X DELETE http://127.0.0.1:5000/api/v1/reviews/<REVIEW_ID>
```


### GET Reviews for Place
```shell
curl http://127.0.0.1:5000/api/v1/places/<PLACE_ID>/reviews
```
---





## TASK 6 – Testing & Validation

### Automated Tests

Run tests with:
```shell
python -m unittest discover -s hbnb/tests
```

Run test_users with:
```shell
python -m unittest hbnb.tests.test_users
```

Run test_places with:
```shell
python -m unittest hbnb.tests.test_places
```

Run test_amenities with:
```shell
python -m unittest hbnb.tests.test_amenities
```
Run test_reviews with:
```shell
python -m unittest hbnb.tests.test_reviews
```



- ### Manual Testing
- Start the Flask application
- Use Postman or curl to test API endpoints
- Verify correct responses and error handling
- Check Swagger documentation for API reference
- http://127.0.0.1:5000/api/v1/

### Conclusion
This implementation provides:
- Clean architecture
- Strict validation
- Full CRUD REST API
- Relationship management
- Automated testing
- Production-ready structure

---
## Authors

- Tommy Jouhans

- James Roussel

---
## Key Strengths of This Implementation

- Clean Architecture
- Strict Validation
- Complete REST API
- Relationship Integrity
- Test Coverage
- Swagger Documentation
- Facade Centralization
- Repository Abstraction
