# HBnb Part 2: Implementation of Business Logic and API Endpoints
## By Tommy JOUHANS and James ROUSSEL

## HBnB – Task 0: Project Setup & Initialization

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

---

#  Project Structure

hbnb/
├── app/
│ ├── init.py # Flask application factory
│ ├── api/
│ │ ├── init.py
│ │ └── v1/
│ │ ├── init.py
│ │ ├── users.py
│ │ ├── places.py
│ │ ├── reviews.py
│ │ ├── amenities.py
│ ├── models/
│ │ ├── init.py
│ │ ├── user.py
│ │ ├── place.py
│ │ ├── review.py
│ │ ├── amenity.py
│ ├── services/
│ │ ├── init.py
│ │ ├── facade.py
│ ├── persistence/
│ ├── init.py
│ ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md


---

# ⚙ Components Description

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


