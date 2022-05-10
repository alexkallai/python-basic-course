class Inventory:
    """
    Class description
    """

    def __init__(self):
        self.inventoryDict: dict = {}

    def addItem(self, name, amount):
        self.inventoryDict.update({str(name):int(amount)})
        print(f"added {name} record with {amount} amount")

    def checkOutItem(self, name: str, amount: int):
        if name in self.inventoryDict:
            self.inventoryDict[name] -= amount
            print(f"'{name}' record was decreased by {amount} in the inventory.")
        else:
            print(f"'The inventory does not contain {name}' record!")

    def listItems(self):
        print("\nThe items in the inventory are:")
        for listItem in self.inventoryDict:
            print(f"\t{listItem} -- {self.inventoryDict[listItem]}")
        print("END\n")
        pass

    def deleteItem(self, name):
        if name in self.inventoryDict:
            self.inventoryDict.pop(name)
            print(f"'{name}' record was deleted from the inventory.")
        else:
            print(f"'{name}' record was NOT deleted from the inventory.")
