print("text formatter")

str = input("enter text that you want to format::")

style = input("choose format style:\n 1.uppercase \n 2.lowercase \n 3.sentencecase \n 4.title (1-4):")

if style == "1":
    print(str.upper())
elif style == "2":
    print(str.lower())
elif style == "3":
    print(str.capitalize())
elif style == "4":
    print(str.title())