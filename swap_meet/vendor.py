
class Vendor:

    def __init__(self,inventory=None):
        self.inventory = inventory or []

    def add(self,item):
        self.inventory.append(item)
        return self.inventory[-1]

    def remove(self,item):
        for i in self.inventory:
            if i == item:
                self.inventory.remove(i)
                return i
        return None

    def get_by_id(self,item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def swap_items(self,other_vendor,my_item,their_item):
        if not my_item and not their_item:
            return False

        if my_item not in self.inventory:
            return False

        if their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        self.add(their_item)

        other_vendor.remove(their_item)
        other_vendor.add(my_item)

        return True

    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_item = self.inventory[0]
        their_item= other_vendor.inventory[0]

        return self.swap_items(other_vendor,my_item,their_item)

        
    def get_by_category(self,category):
        if category is None or category == "" or category == "Unknown":
            return []
        else:
            return [item for item in self.inventory if item.get_category() == category]


    def get_best_by_category(self,category):
        items = self.get_by_category(category)
        if not items:
            return None

        return max(items, key=lambda item: item.condition)

    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False

        return self.swap_items(other_vendor,my_item,their_item)