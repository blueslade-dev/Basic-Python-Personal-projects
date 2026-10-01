import random as r

print("====ROCK PAPER SCISSORS GAME====\n")
print("Hi! User Lets play a game of rock paper scissors!\n")
choices = ['Rock','Paper','Scissors']


while True:
    user_choice = input("Enter a choice (Rock/Paper/Scissors): ").strip().capitalize()
    AI_choice = r.choice(choices)
    if user_choice not in choices:
        print("Invalid choice. Try again")
        continue
    else:
        print("Your choice: ",user_choice)
        break

print("My Choice: ", AI_choice)

if AI_choice == "Rock" and user_choice == "Scissors":
    print(f"Haha my {AI_choice} has smashed your {user_choice}!\nYou LOST!")
elif AI_choice == "Scissors" and user_choice == "Rock":
    print(f"Holy nah your {user_choice} has smashed my {AI_choice}!\nYou WON!")   
elif AI_choice == "Rock" and user_choice == "Paper":
    print(f"No way! You crushed my {AI_choice} with your {user_choice}!\nYou WON!")
elif AI_choice == "Paper" and user_choice == "Rock":
    print(f"Your {user_choice} cannot withstand my mighty {AI_choice}!\nYou LOST!")
elif AI_choice == "Scissors" and user_choice == "Paper":
    print(f"My {AI_choice} have tore your {user_choice} into pieces!\nYou LOST!")
elif AI_choice == "Paper" and user_choice == "Scissors":
    print(f"Dang! Your {user_choice} defeated my {AI_choice}!\nYou WON!")
else:
    print(f"We have tied up! My Choice and your choice ({user_choice}) are the same!\nYou TIED!")

