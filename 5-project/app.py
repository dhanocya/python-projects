print("Grade calculator")
scores = []

while True:
    score = input("enter your score or (done):")
    if score.lower() == "done":
        print("goodbye")
        break

    scores.append(float(score))

    avarege = sum(scores) / len(scores)
    print(f"Avarage score:{avarege:.1f}")

    if avarege >= 90:
        print("grade A")
    elif avarege >= 80:
        print("grade B")
    elif avarege >= 70:
        print("grade C")
    else:
        print("failed or D")