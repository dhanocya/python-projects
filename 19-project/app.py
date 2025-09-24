import random
import time
import os
from colorama import Fore,Back,init,Style

def clear_window():
    os.system("cls" if os.name == "nt" else clear)

print(Fore.YELLOW + Back.GREEN +"Memory Sequence Game")
print("remember the sequnce and type it back?")
print(f"\n")
print(Fore.BLACK + Back.YELLOW +"rules")
print("watch carefully number appear one by one")
print("after the sequnce is shown. type it back")
print("each rounds add one more number for remember")
print("how far you can go?")

input("press enter to start")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1,9))
    clear_window()

    print(f"Current {current_round}")
    print(f"sequnce of {len(sequence)} numbers")

    for number in sequence:
        time.sleep(0.7)
        print(f"\n{number}")
        time.sleep(0.7)
        clear_window()
    print(f"\n now reapeat the sequence of by typing the numbers. seprated by space.")