from colorama import Fore, Back, init, Style
import random

# Colorama को Windows पर ठीक से काम करने के लिए शुरू करें
init(autoreset=True)

# स्कोर के लिए वेरिएबल्स सेट करें
player_score = 0
computer_score = 0
round_count = 0

print(Fore.RED + Back.BLACK + "Rock=Paper=Scissors")
print(Style.RESET_ALL) # रंग को रीसेट करें
print("Rules:")
print("-Rock Crushes Scissors")
print("-Scissors cut paper")
print("-Paper Covers Rock")
print(Fore.CYAN + "First to 3 rounds will be the champion!\n")

# एक 'while' लूप शुरू करें जो तब तक चलेगा जब तक कोई 3 राउंड नहीं जीत जाता
while player_score < 3 and computer_score < 3:
    round_count += 1
    print(Fore.YELLOW + f"--- Round {round_count} ---")
    
    # उपयोगकर्ता से इनपुट लें और इनपुट को मान्य करें
    while True:
        try:
            player_choice = int(input(Fore.GREEN + "Choose your option:\n1. Rock\n2. Paper\n3. Scissors\n" + Fore.WHITE))
            if player_choice in [1, 2, 3]:
                break
            else:
                print(Fore.RED + "Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    # उपयोगकर्ता की पसंद को टेक्स्ट में बदलें
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(Fore.GREEN + f"You chose: {choices[player_choice]}")

    # अब कंप्यूटर अपनी बारी चुनेगा
    computer_choice = random.randint(1, 3)
    print(Fore.BLUE + f"Computer chose: {choices[computer_choice]}")

    # विजेता की जाँच करें
    if player_choice == computer_choice:
        print(Fore.YELLOW + "It's a tie!")
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print(Fore.GREEN + "You win the round!")
        player_score += 1
    else:
        print(Fore.RED + "Computer wins the round!")
        computer_score += 1

    # वर्तमान स्कोर दिखाएँ
    print(Fore.MAGENTA + f"\nCurrent Score: You - {player_score} | Computer - {computer_score}\n")

# खेल खत्म होने के बाद, विजेता की घोषणा करें
print(Fore.CYAN + "--- GAME OVER ---")
if player_score == 3:
    print(Fore.GREEN + Back.WHITE + "Congratulations! You are the champion!")
else:
    print(Fore.RED + Back.WHITE + "The computer is the champion. Better luck next time!")

