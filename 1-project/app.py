print("::website checker::")

while True:
    site = input("enter website URL: ").lower()
    
    if site.startswith("http://"):
        print("Site is not secured")
    elif site.startswith("https://"):
        print("Site is secured")
    else:
        print("please enter valid URL")
        continue

    again = input("check another site (yes/no)").lower()

    if not again.startswith("y"):
        print('goodBye')
        break