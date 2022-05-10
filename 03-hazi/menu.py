import inventory

class Menu:
    """
    Class description
    """

    def __init__(self):
        self.inventoryInstance = inventory.Inventory()
        print("Welcome to the inventory application!")

    def baseState(self):
        print("Please choose from the following options!")
        print("1. List elements")
        print("2. Add element")
        print("3. Remove element")
        print("4. Check out element")


