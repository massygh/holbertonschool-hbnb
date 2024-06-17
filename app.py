#!/usr/bin/python3
"""Entry point for the application."""

from flask import Flask
from flask_restx import Api
from api.api_place import ns as api_place
from api.api_user import ns as api_user
from api.api_review import ns as api_review
from api.api_amenity import ns as api_amenity
from api.api_country import ns as api_country
from api.api_city import ns as api_city

app = Flask(__name__)
ns = Api(app)

# Adding namespaces for each entity
ns.add_namespace(api_place, path='/places')
ns.add_namespace(api_user, path='/users')
ns.add_namespace(api_review, path='/reviews')
ns.add_namespace(api_amenity, path='/amenities')
ns.add_namespace(api_country, path='/countries')
ns.add_namespace(api_city, path='/cities')

#modication for docker
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5002))
    app.run(host="0.0.0.0", port=port)

#Docker
#    app.run(debug=True)