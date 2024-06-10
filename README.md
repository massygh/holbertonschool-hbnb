# HBnb Evolution Project: Part 1

Welcome to the HBnB Evolution Project. This is the first part of our journey in creation a web apptication modeled after AirBnB using Python and Flask.

# table of contents

* Project Overview
* Technoogies Used
* Setup and Installation
* Usage
* Project Structure
* Data Model
* API Endpoints
* Testing
* Docker Packaging
* Authors

# Project Overview

**what's cooking in Part 1?**


1. Sketching with UML: Creating the architectural blueprint of the application n application using UML diagrams.

........add the uml just here........

2. Testing Our Logic: Setting up tests for the API and business logic to ensure smooth operations.
3. Building the API: Implementing the API using Flask that interacts with our business logic and file-based data storage.
4. File-Based Data Storage: Using a file-based system for data storage initialllly, with plans to shift to a database later.
5. Packaging with Docker: Wrapping everything up in a Docker image for easy deployement and portability.

# the three layers of Our API Cake

* **Services Layer**: Handles all requests and responses.
* **Business Logic Layer**: Processes and makes decisions based on the business rules.
* **Persistence Layer**: Manages data storage, initially using a file-based system.

#techniologies Used

* **Python**: Programming language.
* **FlasK**: Web framework for building the API
* **UML**: For architectural design.
* **Docker**: For containerizing the application.
* **uuid**: Python module for generating UUID4.
* **datetime**: Python module for handling timestamps.

#Setup and Installation
## prerequisites

* Python 3.x
* Flask
* Docker (for containerization)

## installation Steps

1. Clone the Repository
2. Set Up Virtual Environment
3. Install Dependencies
4. Run the Application

# Usage
## Running the API

Once the application id set up, you can run the API.

```bash
flask run
```

## API Endpoints
* **GET /places**: Retrieve all places.
* **POST /places**: Create a new place.
* **GET /places/<id>**: Retrieve a place by its ID.
* **PUT /places/<id>**: Update a place by its ID.
* **DELETE /places/<id>**: Delete a place by its ID.
* Other endpoints for Users, Reviews, Amenities, and Cities will be similarly stuctured.

# Project Structure

```bash
HBnB_evolution/
|__ app.py
|__ models/
|	|__ __init__.py
|	|__ place.py
|	|__ user.py
|	|__ review.py
|	|__ amenity.py
|	|__ city.py
|__ tests/
|	|__ __init__.py
|	|__ test_place.py
|	|__ test_user.py
|	|__ test_review.py
|__ Dockerfile
|__ requirements.txt
|__ README.md
```

# Data Model
## Key entities

* **Place**: Characteristics include name, description, address, city, latitude, longitude, host, number of rooms, bathrooms, price per night, max guests, aminities, and reviews.
* **User**: Attributes include email, passmord, first name, and last name. Can be a host or a reviewer.
* **Amenity**: Features like Wi-Fi, pools, etc.
* City and Country: Places are tied to a city, and cities belong to a country.

## Standard Attributes
* **UUID4**: Unique identifier for each entity.
* **created_at**: tumestanp for creation.
* **updated_at**:timestamp for the last update.

# testing
to run tests for the project, we use this line of command 

```bash
pytest
```

# Docker Packaging
to build and run the Docker container:
1. Build Docker Image

```bash 
we must add the line of command
```
2. Run Doker container

```bash
same, ..line of command..
```

# Authors
- [@Fatma Gmati](https://github.com/fatmaGma)
- [@Massy Ghendous](https://github.com/massygh)
- [@Ines Oubabas](https://github.com/Ines-Oubabas)
