#!/usr/bin/python3
# Persistence for users

from model.user import User
from persistence.ipersistence_manager import IPersistenceManager


class UserRepository(IPersistenceManager):
    """Class for managing the persistence of users."""

    def __init__(self):
        """Initializes the UserRepository with an empty
        dictionary and a next_id counter.
        """
        self.users = {}
        self.next_id = 1

    def save(self, user):
        """
        Saves a user.

        If the user does not have a user_id, it assigns a new unique ID.
        The user is then stored in the users dictionary.
        """
        if not hasattr(user, 'user_id'):
            user.user_id = self.next_id
            self.next_id += 1
        self.users[user.user_id] = user

    def get(self, user_id):
        """
        Fetches a user by its ID.

        Args:
            user_id (int): The unique identifier of the user.

        Returns:
            User: The user object if found, otherwise None.
        """
        return self.users.get(user_id)

    def get_all(self):
        """
        Fetches all users.

        Returns:
            list: A list of all user objects.
        """
        return list(self.users.values())

    def update(self, user_id, new_user_data):
        """
        Updates an existing user.

        Args:
            user_id (int): The unique identifier of the user to be updated.
            new_user_data (dict): A dictionary containing
            the new data for the user.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if user_id in self.users:
            user = self.users[user_id]
            user.update_user_data(new_user_data)
            self.save(user)
            return True
        return False

    def delete(self, user_id):
        """
        Deletes an existing user.

        Args:
            user_id (int): The unique identifier of the user to be deleted.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False