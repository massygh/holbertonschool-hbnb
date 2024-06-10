"""
Tests Package

This package contains all the unit tests for the HBnB Evolution project.
Each module in this package tests a specific part of the application's functionality,
including models for users, places, reviews, amenities, cities, and countries.

Modules:
    test_user: Contains tests for the User model.
    test_place: Contains tests for the Place model.
    test_review: Contains tests for the Review model.
    test_amenity: Contains tests for the Amenity model.
    test_city: Contains tests for the City model.
    test_country: Contains tests for the Country model.
"""

# Importing all test modules to ensure they are included when running the tests
from .test_user import TestUser
from .test_place import TestPlace
from .test_review import TestReview
from .test_amenity import TestAmenity
from .test_city import TestCity
from .test_country import TestCountry
