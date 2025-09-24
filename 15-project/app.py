import random
print("**Guess the number**")
print("I am thinking of number between 0 to 100 you have ten attempts to guess the number.")

playing = True
while playing:
    genrate = random.randint(1,100)
    attempts = 0
    maxAttempts = 10

    gameOver = False

    while attempts < maxAttempts and not gameOver:
        try:
            guess = int(input(f"attempts {attempts}/10. guess your number"))
        except ValueError:
            print("XX enter valid number XX")
            continue

        attempts += 1

        if guess < genrate:
            print("too low. guess higher value.")
        elif guess > genrate:
            print("too high. guess lower value.")
        else:
            print(f"congrats! you guess the number {genrate} in {attempts} attempts")
            gameOver = True

    playAgain = input("would you like to play again? (yes/no)").lower()

    if playAgain.startswith("y"):
        print("New game starting...")
    else:
        print("goodbye!")