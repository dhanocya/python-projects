import random

print("*Random recipe genrater*")

ingredents = ["patato","tomato","rice","pulse","mango","cucumber","pumpkin"]
liqudes = ["water","coco","melon","chilli","coconut water","pani patasi","ganga jal"]
main = ["red bull","nibu","burgur","pizza","bornvita"]

while True:
    randomrac = random.choice(ingredents)
    ranLik = random.choice(liqudes)
    randMain = random.choice(main)

    print(f"your random racipe is :{randomrac} {randMain} {ranLik}")

    anRound = input("another recipe? (yes/no)").lower()

    if anRound != "yes":
        print("goodbye!")
        break
    else:
        continue
