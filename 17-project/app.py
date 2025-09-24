
print("::::::::::::::")
print("::Calculator::")
print("::::::::::::::")

def add(numA,numB):
    return numA + numB
def sub(numA,numB):
    return numA - numB
def mul(numA,numB):
    return numA * numB
def div(numA,numB):
    return numA / numB

def main():

    while True:
        print("choose opration.")
        print("1. additon")
        print("2. subtaction")
        print("3. multiplication")
        print("4. diviation")


        while True:
            choice = input("enter your choice (1 to 4):")

            if choice not in ["1","2","3","4"]:
                print("invalid choice! enter valid choice (1 to 4)")
            else:
                break

        try:
            numA = float(input("input a number:"))
            numB = float(input("enter num b:"))
        except ValueError:
            print("enter valid number!")
            continue
        
        if choice == "1":
            print(f"\n {numA} + {numB} = {add(numA,numB)}")
        if choice == "2":
            print(f"\n {numA} - {numB} = {sub(numA,numB)}")
        if choice == "3":
            print(f"\n {numA} * {numB} = {mul(numA,numB)}")
        if choice == "4":
            print(f"\n {numA} / {numB} = {div(numA,numB)}")


        again = input("do you want to do another calculation? (yes/no):").lower()
        if not again.startswith("y"):
            print("goodbye!")
            break
            
main()