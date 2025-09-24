print("step counter")

goal = int(input("input your daily goal:"))
walked = int(input("how many step did you wallked:"))

if goal > walked:
    total = goal - walked
    print(total,"steps needed to complete the goal")
elif goal < walked:
    total = walked - goal
    print("goal is completed you walked extra", total)
else:
    print("goal is completed.")