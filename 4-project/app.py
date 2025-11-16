print("word type checker")

while  True:
    value = input("enter a single charecter:")

    if value.isdigit():
        print("thsi is digit")
    elif value.isalpha():
        print("this is latter")
    else:
        print("this is special charecter.")

    choice = input("try with another charecter(y/n)")

    if not choice.startswith("y"):
        print("come back again")
        break