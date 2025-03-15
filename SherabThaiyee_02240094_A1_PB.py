import random

# 1. Guess the Number Game
def guess_the_number():

    Max = int(input("please put the highest limit of the range: "))
    Min = int(input("please put the lowest limit of the range: "))
    secret_number = random.randint(Min, Max)
    attempts = 0

    print(f"i will guess a number between {Min} and {Max}. if you are genius try a luck!")

    while True:
        try:
            number_guess = int(input("guess a number: "))
            attempts += 1
        except ValueError:
            print("your input is invalid. please try to guess a number.")
            continue

        if number_guess < secret_number:
            print("your guess is TOO HIGH!Try one more time ")

        elif   number_guess > secret_number:
            print("your guess is TOO HIGH! Try one more time")
        else:
            print(f"hurrah! You guessed the right number {secret_number} after {attempts} attempts.")
            break

# 2. Rock Paper Scissors Game
def rock_paper_scissors():
    options = ["paper", "rock", "scissors"]

    while True:
        your_choice = input("Enter your choice (scissors,rock, or paper), or 'q' to quit: ").lower()

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

    user_choice = input(  "if you wish to play another game yes/no :")
    if user_choice != 'yes':
        print("EXIT" )
        break


