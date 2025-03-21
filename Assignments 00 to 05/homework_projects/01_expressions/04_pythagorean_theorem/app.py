"""
Program: Pythagorean Theorem Calculator 📐
------------------------------------------
This program calculates the hypotenuse of a right triangle
using the Pythagorean theorem: BC² = AB² + AC².
"""

import math  # Import math module for sqrt function

def calculate_hypotenuse(ab: float, ac: float) -> float:
    """
    Calculates the hypotenuse (BC) using the Pythagorean theorem.
    """
    return math.sqrt(ab**2 + ac**2)

def main():
    while True:  # Loop for multiple calculations
        try:
            ab = float(input("Enter the length of AB (or type 0 to exit): "))
            if ab == 0:
                print("Exiting program. Goodbye! 👋")
                break

            ac = float(input("Enter the length of AC: "))
            if ac == 0:
                print("Side length cannot be zero! Try again.\n")
                continue  # Restart the loop

            bc = calculate_hypotenuse(ab, ac)  # Calculate hypotenuse

            print(f"The length of BC (the hypotenuse) is: {bc:.2f}\n")

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
