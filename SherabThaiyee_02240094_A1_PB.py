import random

# 1. Guess the Number Game
def guess_the_number():
    '''Plays a number guessing game.'''
    Max = int(input("Enter the upper limit of the range: "))
    Min = int(input("Enter the lower limit of the range: "))
    secret_num = random.randint(Min, Max)
    attempts = 0

    print(f"I'm thinking of a number between {Min} and {Max}. Try to guess it!")

    while True:
        try:
            guess_num = int(input("Enter your number: "))
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess_num < secret_num:
            print("your guess is too low! Try again")

        elif   guess_num > secret_num:
            print("your guess is too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_num} in {attempts} attempts.")
            break

# 2. Rock Paper Scissors Game
def rock_paper_scissors():
    '''Plays a text-based rock-paper-scissors game.'''
    options = ["paper", "rock", "scissors"]

    while True:
        your_choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()

        if your_choice == 'q':
            print("Thank you !")
            break

        if your_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)

        print(f"You chose: {your_choice}")
        print(f"Computer chose: {computer_choice}")

        if your_choice == computer_choice:
            print("It's a tie!")
        elif (
            (your_choice == "scissors" and computer_choice == "papre")
            or (your_choice == "rock" and computer_choice == "scissors")
            or (your_choice == "paper" and computer_choice == "rock")
        ):
            print(" Congratulations You won!")
        else:
            print(" we are sorry ,You lose!")


# Main menu
while True:
    print("\nChoose a game:")
    print("1. Guess the Number")
    print("2. Rock Paper Scissors")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        guess_the_number()
    elif choice == "2":
        rock_paper_scissors()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    user_choice = input("Do you want to play another game yes / no: ")
    if user_choice != 'yes':
        print("Thank you for Playing" )
        break


