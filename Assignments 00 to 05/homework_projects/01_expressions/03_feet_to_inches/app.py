"""
Program: Feet to Inches Converter 📏
------------------------------------
This program converts a given length in feet to inches.
1 foot = 12 inches.
"""

# Define conversion constant
INCHES_IN_FOOT: int = 12  

def convert_feet_to_inches(feet: float) -> float:
    """
    Converts feet to inches.
    """
    return feet * INCHES_IN_FOOT

def main():
    while True:  # Allows multiple conversions
        try:
            feet = float(input("Enter number of feet (or type 0 to exit): "))
            if feet == 0:
                print("Exiting program. Goodbye! 👋")
                break  # Exit the loop if user enters 0

            inches = convert_feet_to_inches(feet)  # Perform conversion
            
            print(f"{feet} feet is equal to {inches} inches!\n")

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
