"""
Program: Triangle Perimeter Calculator
--------------------------------------
This program calculates the perimeter of a triangle based on
user-provided side lengths.
"""

def main():
    # Prompt the user for the side lengths
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Display the result using f-string formatting
    print(f"The perimeter of the triangle is {perimeter}")

# Ensuring main() runs only when the script is executed directly
if __name__ == '__main__':
    main()
