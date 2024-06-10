"""
Models Package

This package contains all the data models used in the HBnB Evolution project.
Each model represents a distinct entity within the application.

Modules:
    user: Contains the User class.
    place: Contains the Place class.
    review: Contains the Review class.
    amenity: Contains the Amenity class.
    city: Contains the City class.
    country: Contains the Country class.
"""

from .user import User
from .place import Place
from .review import Review
from .amenity import Amenity
from .city import City
from .country import Country

# Adding docstrings for each import to explain the purpose of the class

User.__doc__ = """
User Class

Represents a user in the HBnB application. Users can either be hosts or reviewers.

Attributes:
    id (UUID4): Unique identifier for the user.
    email (str): Email address of the user.
    first_name (str): First name of the user.
    last_name (str): Last name of the user.
    password (str): Password for the user account.
    created_at (datetime): Timestamp of when the user was created.
    updated_at (datetime): Timestamp of when the user was last updated.
"""

Place.__doc__ = """
Place Class

Represents a place in the HBnB application, which can be hosted by a user.

Attributes:
    id (UUID4): Unique identifier for the place.
    name (str): Name of the place.
    description (str): Description of the place.
    address (str): Address of the place.
    city_id (UUID4): Identifier of the city where the place is located.
    host_id (UUID4): Identifier of the user hosting the place.
    latitude (float): Latitude of the place location.
    longitude (float): Longitude of the place location.
    number_of_rooms (int): Number of rooms in the place.
    number_of_bathrooms (int): Number of bathrooms in the place.
    price_per_night (float): Price per night for staying at the place.
    max_guests (int): Maximum number of guests that can stay at the place.
    created_at (datetime): Timestamp of when the place was created.
    updated_at (datetime): Timestamp of when the place was last updated.
"""

Review.__doc__ = """
Review Class

Represents a review made by a user for a place in the HBnB application.

Attributes:
    id (UUID4): Unique identifier for the review.
    place_id (UUID4): Identifier of the place being reviewed.
    user_id (UUID4): Identifier of the user who wrote the review.
    text (str): Text of the review.
    rating (int): Rating given to the place.
    created_at (datetime): Timestamp of when the review was created.
    updated_at (datetime): Timestamp of when the review was last updated.
"""

Amenity.__doc__ = """
Amenity Class

Represents an amenity that a place can have in the HBnB application.

Attributes:
    id (UUID4): Unique identifier for the amenity.
    name (str): Name of the amenity.
    description (str): Description of the amenity.
    created_at (datetime): Timestamp of when the amenity was created.
    updated_at (datetime): Timestamp of wh
