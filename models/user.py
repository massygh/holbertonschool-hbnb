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

    def createUser(self):
        pass  # implementation of user creation

    def deleteUser(self):
        pass  # implementation of user deletion

    @staticmethod
    def is_email_unique(email):
        pass  # Logic to check if the email is unique in the system
