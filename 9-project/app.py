import random
print("name reverser::")

while True:
    name = input("enter a name:")
    reversedName = name[::-1]

    print("your reversed name is",reversedName)
    print("in other universe they call you",reversedName)

    again = input("turn another name in reverse (y/n)").lower()

    if not again.startswith("y"):
        print("good Bye")
        break