"""
Run Module

This is the entry point of the HBnB Evolution application. It initializes the
Flask application, configures the routes, and starts the server.
"""

from flask import Flask
from api import app as api_app
from api.user_api import user_app
from api.country_city_api import country_city_app

# Initialize Flask application
app = Flask(__name__)

# Configure the application with the API routes
app.register_blueprint(api_app)
app.register_blueprint(user_app, url_prefix='/api/v1')
app.register_blueprint(country_city_app, url_prefix='/api/v1')

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
