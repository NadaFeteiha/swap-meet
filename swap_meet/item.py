import uuid



# - Instances of `Vendor` have an instance method named `swap_items`
#   - It takes 3 arguments:
#   - `swap_items` takes 3 arguments:
#     1. an instance of another `Vendor` (`other_vendor`), representing the friend that the vendor is swapping with
#     2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
#     3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give

#   - The method removes `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
#   - The method removes `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
#   - The method returns `True`
#   - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`



class Item:

    def __init__(self,id= None, condition=0):
        if not id :
            self.id = uuid.uuid4().int
        else:
            self.id = id

        # Initialize the condition of the item
        self.condition = condition


    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        if self.condition == 0:
            return "Unusable"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Very Good"
        elif self.condition == 5:
            return "Excellent"

    