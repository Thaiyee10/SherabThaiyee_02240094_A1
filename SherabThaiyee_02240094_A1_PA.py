import math
import requests

# Prime number sum calculator
def is_prime(n):
   
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


    """Checks if a number is prime.
        n: The number to check.
        True if the number is prime, False otherwise."""
    
def prime_sum(start, end):
    
    if not isinstance(start, int) or not isinstance(end, int) :
        return "Invalid Input. Start and end must be integers"
    if start > end :
        return "Invalid Input. Start must be less than or equal to End"
    return sum(n for n in range(start, end + 1) if is_prime(n))
    
    """Calculates the sum of prime numbers within a given range.
        start: The starting number of the range.
        end: The ending number of the range.
        The sum of prime numbers in the range."""
# Lenght unit converter
def convert_length_units(value, direction):
    
    if not isinstance(value, (int, float)):
        return "Invalid input. Value must be a number."
    if direction not in ('F', 'M'):
        return "Invalid direction. Use 'F' or 'M'."
    if direction == 'F':
        return round(value / 3.28084, 2)
    elif direction == 'M':
        return round(value * 3.28084, 2)
    
    """ Converts length units between meters and feet.
        value: The length value to convert.
        direction: 'F' for feet to meters, 'M' for meters to feet.
        The converted length value, or an error message if invalid input."""
    
#Counsonent counter
def tally_consonants(text):
    
    if not isinstance(text, str):
        return "Invalid input. Text must be a string."
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
    
    """ Counts the number of consonants in a given text.
        text: The text to analyze.
        The number of consonants in the text."""
    
 #Finding min max number
def min_max_finder(numbers):
   
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        return "Invalid input. Numbers must be a list of numbers."
    if not numbers:
        return "List is empty"
    return min(numbers), max(numbers)
    """ Finds the minimum and maximum numbers in a list.
        numbers: A list of numbers.
        A tuple containing the minimum and maximum numbers."""
    
 #pelindrome checker
def verify_palindrome(text):
    
    if not isinstance(text, str):
        return "Invalid input. Text must be a string."
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]
   
    """Finds the minimum and maximum numbers in a list.
        numbers: A list of numbers.
        A tuple containing the minimum and maximum numbers."""
    
 #word counter
def word_counter(text_file_url):
   
    if not isinstance(text_file_url, str):
        return "Invalid input. URL must be a string."
    try:
        response = requests.get(text_file_url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        text = response.text.lower()
        word_list = ["the", "was", "and"]
        word = {word: text.count(word) for word in word_list}
        return word
    except requests.exceptions.RequestException as e:
        return f"Error fetching the file: {e}"
    
    """Counts the occurrences of specified words in a text file from a URL.
        text_file_url: The URL of the text file.
        A dictionary containing the word counts, or an error message if invalid URL."""
    
#Main menu
def main():
    """
    Main function to run the program.
    """
    while True:
        print("""
        Select a function:
        1. Prime number sum calculator
        2. Length unit converter
        3. Consonant counter
        4. Min-Max number finder
        5. Palindrome checker
        6. Word counter from file
        7. Exit
        """)
        choice = input("Enter your choice from 1 to 7: ")

        if choice == '1':
            try:
                start = int(input("Enter lowest limit: "))
                end = int(input("Enter highest limit: "))
                result = prime_sum(start, end)
                print("Sum of primes:", result)
            except ValueError:
                print("Invalid input. Please enter integer values.")

        elif choice == '2':
            try:
                print("Type M for convert meter to Feet")
                print("Type F for convert feet to meter")
                value = float(input("Enter value: "))
                direction = input("Enter M/F: ").upper()
                print(f"Converted value: {convert_length_units(value, direction)}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            text = input("Enter text: ")
            print("Number of consonants:", tally_consonants(text))

        elif choice == '4':
            try:
                n = int(input("How many numbers? "))
                numbers = [float(input(f"Enter number {i+1}: ")) for i in range(n)]
                result = min_max_finder(numbers)
                if isinstance(result, str):
                    print(result)
                else:
                    min_num, max_num = result
                    print(f"Smallest: {min_num}, Largest: {max_num}")
            except ValueError:
                print("Invalid input. Please enter numbers.")

        elif choice == '5':
            text = input("Enter text: ")
            print("This is palindrome (true / false):", verify_palindrome(text))

        elif choice == '6':
            file_url = input("Enter the URL of the text file: ").strip()
            result = word_counter(file_url)
            print(f"Word count: {result}")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1-7.")

        choice = input("Do you want to try another function (yes / no): ")
        if choice.lower() != 'yes':
            print("Exit")
            break

if __name__ == "__main__":
    main()