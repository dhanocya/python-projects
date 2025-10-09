from colorama import Fore,Back,init,Style
import random

print(Fore.RED + Back.BLACK + "Rock=Papar=Scissors")
print("Rules:")
print("-Rock Crushes Scissors")
print("-Scissors cut paper")
print("-Paper Covers Rock")
print("first 3 round will be the champion")

def play():
    print("round 1")
    print("make your choise:")
    print("Rock")
    print("paper")
    print("scissors")

    choose = int(input("choose your otion 1 to 4"))
    print(choose)

    if choose == 1:
        print("you choosed rock")
    elif choose == 2:
        print("you choosed paper")
    else:
        print("you choosed scissors")

play()

# now lets computer will choose the otion

def computerTurn():
    return random.randint(1,6)

computerTurn()

