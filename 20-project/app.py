from colorama import Fore,Back,init,Style
import random

print(Fore.RED + Back.BLACK + "Rock=Papar=Scissors")
print("Rules:")
print("-Rock Crushes Scissors")
print("-Scissors cut paper")
print("-Paper Covers Rock")
print("first 3 round will be the champion")

def play():
    print("round ")
    print("make your choise:")
    print("Rock")
    print("paper")
    print("scissors")

play()

choose = int(input("choose your otion 1 to 4"))
print(choose)

if choose == 1:
    print("you choosed rock")
elif choose == 2:
    print("you choosed paper")
else:
    print("you choosed scissors")

# now lets computer will choose the otion

def computerTurn():
    return random.randint(1,3)

hold = computerTurn()

def checkScore():
    if hold == 1:
        print("computer choosed rock")
    elif hold == 2:
        print("computer choosed paper")
    else:
        print("computer choosed scissors")

checkScore()

def answer():
    if choose > hold:
        print("player win")

answer()