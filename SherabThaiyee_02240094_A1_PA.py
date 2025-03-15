import math

def prime_sum_calculator(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    return sum(n for n in range(start, end + 1) if prime_sum_calculator(n))

def convert_length_units(value, direction):
    if direction == 'F':
        return round(value / 3.28084, 2)
    elif direction == 'M':
        return round(value * 3.28084, 2)
    else:
        return "Invalid direction."
def tally_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def min_max_finder(numbers):
    return min(numbers), max(numbers)

def verify_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]  

#Woed counter 
import requests
def word_counter(text_file_url):
    response = requests.get(text_file_url)
    text = response.text.lower()
    word_list = ["the", "was", "and"]
    word = {word: text.count(word) for word in word_list}

    return word 

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
            start = int(input("enter lowest limit: "))
            end = int(input("enter highest limit: "))
            print("Sum of primes:", prime_sum(start, end))
        
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
            n = int(input("How many numbers? "))
            numbers = [float(input(f"Enter number {i+1}: ")) for i in range(n)]
            min_num, max_num = min_max_finder(numbers)
            print(f"Smallest: {min_num}, Largest: {max_num}")
        
        elif choice == '5':
            text = input("Enter text: ")
            print(" This is  palindrome (true / false):", verify_palindrome(text))
        
        elif choice == '6':
            #word counter

            file_url = input("Enter the URL of the text file: ").strip()
            try:
                result = word_counter(file_url)
                print(f"word count:{result}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching the file: {e}")
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-7.")

        choice = input ("do you want to try another function (yes / no) : ")
        if choice != 'yes':
             print("Thank you")
             break

if __name__ == "__main__":
    main()



 


