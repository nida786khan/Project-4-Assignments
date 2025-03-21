"""
Program: Einstein's Mass-Energy Equivalence 💡
---------------------------------------------
This program continuously asks the user to enter mass (in kg) and calculates 
the equivalent energy using Einstein's famous equation: E = m * c^2.

The speed of light (C) is considered as a constant: 299,792,458 m/s.
"""

# Define the speed of light constant in meters per second
SPEED_OF_LIGHT = 299_792_458  # Underscores improve readability (Python 3.6+)

def calculate_energy(mass: float) -> float:
    """
    Calculates the energy equivalent of the given mass using Einstein's formula.
    E = m * c^2
    """
    return mass * (SPEED_OF_LIGHT ** 2)

def main():
    while True:  # Keeps running until user provides valid input
        try:
            mass = float(input("Enter kilos of mass (or type 0 to exit): "))
            if mass == 0:
                print("Exiting program. Goodbye! 👋")
                break  # Exit the loop if the user enters 0
            
            energy = calculate_energy(mass)  # Calculate energy
            
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {SPEED_OF_LIGHT} m/s\n")
            print(f"{energy:.2e} joules of energy!\n")  # Displays energy in scientific notation
            
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
