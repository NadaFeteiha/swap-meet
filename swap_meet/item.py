import uuid

class Item:
    CONDITION_DESCRIPTIONS = {
        0: "Unusable",
        1: "Poor",
        2: "Fair",
        3: "Good",
        4: "Very Good",
        5: "Excellent"
    }

    def __init__(self, id=None, condition=0.0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        return self.CONDITION_DESCRIPTIONS.get(int(self.condition), "Unknown")
