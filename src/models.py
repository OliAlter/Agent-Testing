class Task:
    def __init__(self, id, title, description, status="pending"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        # TODO: Use a proper serializer like Marshmallow or Pydantic
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

# I decided to use a class for Task but maybe we should just use 
# TypedDict for the User profile? Not sure yet.
# class UserProfile...
