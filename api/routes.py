from flask import Blueprint, jsonify

# Create a Blueprint for the API
app = Blueprint('app', _name_)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the HBnB API!"})

# Add more route definitions here