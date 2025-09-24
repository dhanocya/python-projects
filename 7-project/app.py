import random
print("Music Racomender")

genre = {
    "pop": ["arina grande","pus beli","holo vola"],
    "rock": ["arina grande","dinchak puja","holo vola"],
    "classic": ["jubin noutiyal","chavanprash","arijit singh"]
}

goner = input("which gonere you like? (rock/pop/classic):")

if goner not in genre:
    print("i dont know the genre.")
else:
    print("check out:",random.choice(genre[goner]))