import random

print("Welcome to the Even-Odd Game!")
print("You will choose 'even' or 'odd' and pick a number (1-10).")
print("The computer will also choose a number.")
print("If the sum is what you guessed, you win!\n")
print("Type 'quit' anytime to stop.\n")

user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose 'even' or 'odd': ").strip().lower()
    if user_choice == 'quit':
        break
    if user_choice not in ['even', 'odd']:
        print("Invalid choice. Type 'even' or 'odd'.\n")
        continue

    user_number_input = input("Enter your number (1 to 10): ")
    if user_number_input.lower() == 'quit':
        break
    if not user_number_input.isdigit():
        print("Please enter a valid number.\n")
        continue

    user_number = int(user_number_input)
    if user_number < 1 or user_number > 10:
        print("Number must be between 1 and 10.\n")
        continue

    computer_number = random.randint(1, 10)
    total = user_number + computer_number

    print("You chose:", user_number)
    print("Computer chose:", computer_number)
    print("Total:", total)

    if total % 2 == 0:
        result = 'even'
    else:
        result = 'odd'

    if user_choice == result:
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

print("\nFinal Score:")
print("You:", user_score)
print("Computer:", computer_score)
print("Thanks for playing!")
