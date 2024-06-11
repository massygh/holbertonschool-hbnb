"""
API Package

This package contains all the modules related to the API of the HBnB Evolution project.
The API package handles the interaction between the client and the server, processing
requests and returning responses.

Modules:
    routes: Contains the general route definitions for the API.
    user_api: Contains the user-related route definitions for the API.
"""

from flask import Blueprint

# Create a Blueprint for the general API
app = Blueprint('app', __name__)

# Route to check if API is working
@app.route('/')
def index():
    return {"message": "Welcome to the HBnB API!"}
