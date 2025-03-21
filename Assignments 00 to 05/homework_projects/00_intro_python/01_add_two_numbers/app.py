"""
Program: Sum of Two Numbers
---------------------------
This Python program takes two integer inputs from the user,
calculates their sum, and displays the result.
"""

def main():
    print("Welcome! Let's add two numbers.")
    
    # Taking user input and converting to integer
    first_number = int(input("Please enter the first integer: "))
    second_number = int(input("Please enter the second integer: "))

    # Calculating sum
    result = first_number + second_number

    # Displaying the result
    print(f"The sum of {first_number} and {second_number} is {result}.")

# Ensuring main() runs only when the script is executed directly
if __name__ == '__main__':
    main()
