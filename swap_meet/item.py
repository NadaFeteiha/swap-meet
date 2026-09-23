import uuid

class Item:

    def __init__(self,id= None, condition=0.0):
        self.CONDITION_DESCRIPTIONS = {
                0.0: "Unusable", 
                1.0: "Poor",  
                2.0: "Fair",
                3.0: "Good",
                4.0: "Very Good",
                5.0: "Excellent"
            }
        
        if not id :
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition


    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        return self.CONDITION_DESCRIPTIONS.get(self.condition, "Unknown")

    