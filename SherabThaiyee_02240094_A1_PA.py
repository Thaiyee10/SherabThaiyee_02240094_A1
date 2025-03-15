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

def prime_sum(start, end):
    return sum(n for n in range(start, end + 1) if is_prime(n))
    
'''This function is used to test for prime number by evaluating each number fro the given range of numbers 
by the user'''
  
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
    

'''this function is used to convert a given value into desired units (fee,meter)
this is used by asking the user whether they wnat to convert meter to fed or feet to meter 
then the program will ask the value you want to convert  '''
    
#Counsonent counter
def tally_consonants(text):
    
    if not isinstance(text, str):
        return "Invalid input. Text must be a string."
    VOWELS = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in VOWELS:
            count += 1
    return count
    '''this function is used to count the number of consonents from a word given by the user 
    it works by asking for an input specifically a string where by the program will evaluate the strig to check for non vowel words 
    then the program will ignore all the vowels as givne above and count the remaining consonents'''
    
 #Finding min max number
def min_max_finder(numbers):
   
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        return "Invalid input. Numbers must be a list of numbers."
    if not numbers:
        return "List is empty"
    return min(numbers), max(numbers)
  
  
  
  
'''to find min max number this function will ask for a range of input from the user ,
  Basically asking for how many numbers are there in the range then the program will sort out the numbers from least to greatest 
  and rule out the extremes which are the min and max value'''
    
 #pelindrome checker
def verify_palindrome(text):
    
    if not isinstance(text, str):
        return "Invalid input. Text must be a string."
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]
   
'''This function converts the strings given by the users by changing it into lower case letter and removing all the spaces then the program will reverse the string .
   after that the program will compare old sstring to the new string ,if the old and the new string are equal then the program will shoot out that the given string is palindrome'''
    
 #word counter
def word_counter(text_file_url):
   
    if not isinstance(text_file_url, str):
        return "Invalid input. URL must be a string."
    try:
        response = requests.get(text_file_url)
        response.raise_for_status() 
        text = response.text.lower()
        word_list = ["the", "was", "and"]
        word = {word: text.count(word) for word in word_list}
        return word
    except requests.exceptions.RequestException as e:
        return f"Error fetching the file: {e}"
'''The given function will ask for the user to give URL and the program will then read the text file and regcognise the 
    specific strings that are to be identify then the result will be the number of times the desired strings is counted'''
    
#Main menu
def main():
    
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
                print("Invalid input. Please enter between 1-7")

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

main()