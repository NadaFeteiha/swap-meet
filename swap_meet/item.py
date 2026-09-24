import uuid

class Item:
    CONDITION_DESCRIPTIONS = [
        (5, "Excellent"),
        (4, "Very Good"),
        (3, "Good"),
        (2, "Fair"),
        (1, "Poor"),
        (0, "Unusable")
    ]

    def __init__(self, id=None, condition=0.0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        for minimum, description in self.CONDITION_DESCRIPTIONS:
            if self.condition >= minimum:
                return description
        return "Unknown"
