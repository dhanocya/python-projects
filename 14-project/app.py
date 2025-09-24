import random
print("*:*:Guess the word:*:*")

words = ["computer","Science","good boy","coding","Update","mango","spiderwoman","pokemon"]

while True:
    orignal_word = random.choice(words)

    latters = list(orignal_word)
    random.shuffle(latters)

    scrumbled = "".join(latters)
    print(f"scrumbled word: {scrumbled}")

    guess = input("guess the word?: ").lower()

    if orignal_word == guess:
        print("you won!")
    else:
        print(f"sorry wrong,, word is: {orignal_word}")

    again = input("another round? (yes/no)").lower()

    if not again.startswith("y"):
        print("goodbye!")
        break
    else:
        continue