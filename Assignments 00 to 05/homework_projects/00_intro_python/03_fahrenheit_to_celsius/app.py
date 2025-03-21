"""
Program: Fahrenheit to Celsius Converter
-----------------------------------------
This program converts a user-inputted temperature from 
Fahrenheit to Celsius using the standard conversion formula.
"""

def main():
    # Prompting the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: ").strip())

    # Converting to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Displaying the result
    print(f"Temperature: {fahrenheit:.1f}°F = {celsius:.2f}°C")

# Ensuring main() runs only when the script is executed directly
if __name__ == '__main__':
    main()
