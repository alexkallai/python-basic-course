import datetime

def hello_xy(name: str = "defaultname") -> str: # -> str: visszatérési érték definiálva
    #name: str = input("What is your name: ")
    if name == "defaultname":
        name = input("What is your name: ")
    else:
        print("I know you!")
    return f"{datetime.datetime.now()} - Hello {name}!"

print(hello_xy(name = "myname"))
print(hello_xy(name = "defaultname"))
print(hello_xy("myname"))
