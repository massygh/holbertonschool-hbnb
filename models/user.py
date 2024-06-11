import uuid
from datetime import datetime

class User:
    def __init__(self, email, first_name, last_name, password):
        self.id = uuid.uuid4()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the user object to a dictionary.
        """
        return {
            'id': str(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    def update(self, email=None, first_name=None, last_name=None, password=None):
        """
        Update the user attributes.
        """
        if email:
            self.email = email
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if password:
            self.password = password
        self.updated_at = datetime.now()

    @staticmethod
    def is_email_unique(email, users):
        """
        Check if the email is unique among a list of users.
        """
        for user in users:
            if user.email == email:
                return False
        return True

    def createUser(self):
        pass  # implementation of user creation

    def deleteUser(self):
        pass  # implementation of user deletion
