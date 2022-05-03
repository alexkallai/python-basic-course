
class InventoryBase:
    """
    This class can be used as a basic inventory
    """

    def __init__(self):
        self.storageDict = {"initialized_item":1}

    def addItem(self, name, amount):
        self.storageDict.update({str(name):int(amount)})
        print(f"added {name} record with {amount} amount")

    def checkOutItem(self, name: str, amount: int):
        self.storageDict[name] -= amount
        print(f"'{name}' record was decreased by {amount} in the inventory.")

    def listItems(self):
        print("\nThe items in the inventory are:")
        for listItem in self.storageDict:
            print(f"{listItem} -- {self.storageDict[listItem]}")
        print("END\n")
        pass

    def deleteItem(self, name):
        self.storageDict.pop(name)
        print(f"'{name}' record was deleted from the inventory.")


def main():
    # Instantiate the class
    inventory = InventoryBase()

    inventory.listItems()

    inventory.addItem("kalapacs", 6)
    inventory.addItem("veso", 3)
    inventory.listItems()

    inventory.checkOutItem("veso", 2)
    inventory.listItems()

    inventory.deleteItem("veso")
    inventory.listItems()

if __name__ == "__main__":
    main()
