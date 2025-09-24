import time
print("**Countdown**")

while True:
    seconds = int(input("start countdown form: "))

    if seconds <= 0:
        print("please enter possitive value.")
        continue

    print(f"starting countdown from:{seconds}")

    for i in range(seconds,0,-1):
        print(f"{i} seconds remainig...")
        time.sleep(1)
    
    print("Countdown completed!")

    again = input("do you want to set new count down? (yes/no)::")

    if again.startswith("y"):
        print("starting new count down::")
    else:
        print("goodbye!")
        break