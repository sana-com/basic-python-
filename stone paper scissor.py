import random

print("Welcome to Stone Paper Scissors Game!")
print("Enter your choice: stone, paper, or scissors")
print("Type 'exit' to quit the game.\n")

# Score tracking
user_score = 0
computer_score = 0

while True:
    choices = ['stone', 'paper', 'scissors']
    user_input = input("Your turn: ").lower()

    if user_input == 'exit':
        print("\nExiting game...")
        break

    if user_input not in choices:
        print("Invalid input. Please choose stone, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_input == computer_choice:
        print("It's a tie!\n")
    elif (
        (user_input == 'stone' and computer_choice == 'scissors') or
        (user_input == 'scissors' and computer_choice == 'paper') or
        (user_input == 'paper' and computer_choice == 'stone')
    ):
        print("You win this round!\n")
        user_score += 1
    else:
        print("You lose this round.\n")
        computer_score += 1

# Final Score
print("Game Over!")
print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("You lost the game. Try again!")
else:
    print("It's a draw!")
