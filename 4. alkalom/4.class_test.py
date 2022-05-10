
class VariableClass:

    classVar = 1

    def __init__(self):
        self.classVar = 2

    def classVarChanger(self):
        self.classVar = 3

def main():

    print(VariableClass.classVar)
    instantiatedClass = VariableClass()
    print(instantiatedClass.classVar)
    print(instantiatedClass.classVarChanger())
    print(instantiatedClass.classVar)
    VariableClass.classVar = 4
    print(instantiatedClass.classVar)
    instantiatedClass2 = VariableClass()
    print(instantiatedClass2.classVar)
    print(VariableClass.classVar)


if __name__ == "__main__":
    main()