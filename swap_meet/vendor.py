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
        # if not my_item and not their_item:
        #     return False

        if my_item not in self.inventory:
            return False

        if their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        self.add(their_item)

        other_vendor.remove(their_item)
        other_vendor.add(my_item)

        return True
        
        
