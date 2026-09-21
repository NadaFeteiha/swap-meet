
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
