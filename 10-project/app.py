print("vowel counter::::::::::::::::::::::")

while True:
    string = input("enter a word (quit):").lower()

    if string.startswith("quit"):
        print("goodBye")
        break

    vowelCount = 0

    for i in string.lower():
        if i in ['a',"e","o","i","u","A","E","O","I","U"]:
            vowelCount += 1
        
    print(f"that text have {vowelCount} vowels in it")