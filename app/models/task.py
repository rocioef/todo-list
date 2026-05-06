from app.models.status import Status

class Task:
    def __init__(self, id, description, status=Status.TODO):
        self.id = id
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            description = data["description"],
            status = Status(data["status"])
        )