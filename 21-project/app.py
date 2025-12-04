import random
print(":: age calculator ::")

while True:
    bornYear = int(input("enter your dob year ex: 2000 "))
    currentYear = int(input("enter current year: ex: 2045 "))

    if bornYear > currentYear:
        print("please enter correct data.")
        continue

    currentAge = currentYear - bornYear

    print(f"you are now {currentAge} year old")

    choice = input("check one more time? (y/n)")

    if not choice.startswith("y"):
        box = ("good day","magical day","nice day","fun day")
        randnum = random.randint(0,3)
        print(f"you have {box[randnum]}")
        break
