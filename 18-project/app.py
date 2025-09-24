import random
import time

print(":: word link game ::")

wordList = {
    "tree":["leaf","green","nature","wood"],
    "sky":["blue","white","beautiful","nature"],
    "man":["woman","human"]
}

score = 0 
rounds = 0

while True:
        ranWord = random.choice(list(wordList.keys()))
        relatedWords = wordList[ranWord]
        print(f"your word is ::{ranWord}::")

        startTime = time.time()

        answer = input("guess related word?::").lower().strip()
        responseTime = time.time() - startTime

        print("response time", responseTime)

        if answer in relatedWords:
                print("you win")
                points = max(1,5 - int(responseTime))
                score += points
        else:
                print("you loose.")

        rounds += 1
        print(f"your score:{score},rounds::{rounds}")
        
        if input("lets play again? (yes/no)").lower().startswith("n"):
                print("final score::", score ,"thanks for playing!")
                break