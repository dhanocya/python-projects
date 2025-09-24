import random

print("::Color Mixer::")

colors = {
    ("red","blue"):"purple",
    ("red","yellow"):"orange",
    ("blue","yellow"):"green",
    ("red","white"):"pink",
    ("red","green"):"brown",
}

while True:
    color1 = input("enter 1th color: ").lower()
    color2 = input("enter 2th color: ").lower()

    if (color1,color2) in colors:
        mix = colors[(color1,color2)]

        print(f"when you mix {color1} and {color2} you get {mix}")

        again = input("mix more colors? (yes/no)").lower()
        if again != "yes":
            print("Goodbye!")
            break
    else:
        print("::enter valid color name::")