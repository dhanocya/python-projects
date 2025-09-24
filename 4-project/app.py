print("word type checker")

value = input("enter a single charecter:")

if value.isdigit():
    print("thsi is digit")
elif value.isalpha():
    print("this is latter")
else:
    print("this is special charecter.")