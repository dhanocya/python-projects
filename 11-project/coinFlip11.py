import random
print(f"::COIN FLIP GAME::\n **guess tail or head?**")

while True:
    guess = input("guess 'head' or 'tail'")

    if guess != "head" and guess != "tail":
        print("please enter head or tail")
        continue
  
    flip = random.choice(["head","tail"])
    print(f"coin shows {flip}")

    if guess == flip:
        print("you won!")
    else:
        print("incorrect guess")

    again = input("wrong guess try again? (yes/no)").lower()

    if not again.startswith("yes"):
        print("goodbye")
    else:
        continue
    
    break