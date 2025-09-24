import random

print("Word Scrambler")

while True:
    word = input("enter a word to scrambler or (done): ").lower()

    if word.startswith("done"):
        print("Goodbye!")
        break

    later = list(word)
    random.shuffle(later)

    print(f"Scrubled word: {"".join(later)}")