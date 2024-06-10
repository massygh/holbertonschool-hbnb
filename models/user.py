from datetime import datetime

class User:
    _email_set = set()
    
    def __init__(self, user_id, email, name):
        if email in User._email_set:
            raise ValueError("L'email doit être unique")
        self.user_id = user_id
        self.email = email
        self.name = name
        User._email_set.add(email)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_email(self, new_email):
        if new_email in User._email_set:
            raise ValueError("L'email doit être unique")
        User._email_set.remove(self.email)
        self.email = new_email
        User._email_set.add(new_email)
        self.updated_at = datetime.now()
