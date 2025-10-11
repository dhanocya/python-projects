from colorama import Fore, Style, init, Back
init(autoreset=True)

print(Fore.YELLOW+ Back.RED + Style.BRIGHT + "Recharge Calculator ::::::::::::::::::::::::::::::::::::::::::::::::::::")

while True:
    spendMoney = int(input("how much money do you pay for one month recharge? "))
    muchTime = int(input("how many days recharge valid for? "))
    muchData = float(input("how much data you get (gb)"))
    peroid = int(input("how much calculation of months you want to perform (e.g 12)"))

    totalMoney = spendMoney * peroid
    print(Fore.BLUE + Back.GREEN + Style.BRIGHT +"Report data ::::::::::::::::::::::::::::::::::::::::::::::::::::")
    
    if peroid == 12:
        print("cost of 1 year >>", totalMoney)
    elif peroid in ["1","2","3","4","5","6","7","8","9","10","11"]:
        print(f"const of {peroid} month >>",totalMoney)

    # now lets calculate how much net we will get.

    totalNet = muchTime * muchData
    yearNet = totalNet * 12
    print("a month data >>", totalNet)
    print("a year data >>", yearNet)

    break

choice = input("do you want to calculate another reachage plan? (yes/no)")

if choice.startswith("y"):
    print("hello i am working")
else:
    print("have nice day 💕")