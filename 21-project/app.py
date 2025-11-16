print(":: age calculator ::")

def runAgain():
    while True:
        bornYear = int(input("enter your dob year ex: 2000 "))
        currentYear = int(input("enter current year: ex: 2045 "))

        if bornYear > currentYear:
            print("please enter correct data.")
            runAgain()

        currentAge = currentYear - bornYear

        print(f"you are now {currentAge} old")

runAgain()