import uuid

class Country:
    def __init__(self, code, name):
        self.id = uuid.uuid4()
        self.code = code
        self.name = name

    def to_dict(self):
        return {
            'id': str(self.id),
            'code': self.code,
            'name': self.name,
        }
