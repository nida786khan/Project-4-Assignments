"""
Program: Division & Remainder Calculator ➗
-------------------------------------------
This program asks the user for two numbers, 
performs integer division, and prints both 
the quotient and remainder.
"""

def main():
    while True:  # Loop for multiple calculations
        try:
            dividend = int(input("Please enter an integer to be divided (or type 0 to exit): "))
            if dividend == 0:
                print("Exiting program. Goodbye! 👋")
                break

            divisor = int(input("Please enter an integer to divide by: "))
            if divisor == 0:
                print("Error: Division by zero is not allowed! Try again.\n")
                continue  # Restart the loop

            quotient = dividend // divisor  # Integer division
            remainder = dividend % divisor  # Modulo operation

            print(f"The result of this division is {quotient} with a remainder of {remainder}\n")

        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
