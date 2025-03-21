"""
Program: Square Calculator
--------------------------
This program asks the user for a number and prints its square.
"""

def main():
    # Prompt user for input
    number = float(input("Enter a number to find its square: "))

    # Calculate the square
    square = number ** 2

    # Display the result using f-string
    print(f"{number} squared is {square}")

# Ensuring main() runs only when the script is executed directly
if __name__ == '__main__':
    main()
