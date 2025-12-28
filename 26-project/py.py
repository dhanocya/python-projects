print("::::calculator:::::")
while True:
    numA = int(input("enter a number: "))
    numB = int(input("enter b number: "))

    def calculate(numA,ans,numB):
        if ans == 1:
            print(numA + numB)
        elif ans == 2:
            print(numA - numB)
        elif ans == 3:
            print(numA * numB)
        elif ans == 4:
            print(numA / numB)

    print("choose your option (1-4)")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    ans = int(input("enter your choice? (1-4)"))

    check = [1,2,3,4]
    if ans in check:
        calculate(numA,ans,numB)
    else:
        continue

    ask = input("do you want to do another opration? (yes/no): ")

    if ask.startswith("n"):
        print("goodbye")
        break;
    else:
        continue