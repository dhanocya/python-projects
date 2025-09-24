import random
print("@ Fantasy name genrator @")

name = int(input("how much name you want to generate?: "))

nameData = ["Split","Bone","Green","Pro","Monster","Boom","Chadi","Demon","Singer","Finolo","Brain","Cell","Joker"]

for i in range(name):
    aName = random.choice(nameData)
    bName = random.choice(nameData)
    print(f"{aName}{bName}")