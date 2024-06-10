import uuid
from datetime import datetime

class Review:
    def __init__(self, place_id, user_id, text, rating):
        self.id = uuid.uuid4()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def createReview(self):
        pass  # implementation of review creation

    def deleteReview(self):
        pass  # implementation of review deletion
