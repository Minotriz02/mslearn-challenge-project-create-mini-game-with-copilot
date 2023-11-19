import random

def get_user_choice():
    return input("Enter your choice (rock/paper/scissors) or 'finish' to end the game: ")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "User wins!", 1
    else:
        return "Computer wins!", -1

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    if user_choice.lower() == "finish":
        break
    elif user_choice.lower() not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    computer_choice = get_computer_choice()

    print(f"User chose {user_choice}, computer chose {computer_choice}.")
    result, winner = determine_winner(user_choice, computer_choice)
    print(result)

    if winner == 1:
        user_score += 1
    elif winner == -1:
        computer_score += 1

print(f"Final scores: User - {user_score}, Computer - {computer_score}")