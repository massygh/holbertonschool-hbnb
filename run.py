"""
Run Module

This is the entry point of the HBnB Evolution application. It initializes the
Flask application, configures the routes, and starts the server.
"""

from flask import Flask
from api import app as api_app

# Initialize Flask application
app = Flask(__name__)

# Configure the application with the API routes
app.register_blueprint(api_app)

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
