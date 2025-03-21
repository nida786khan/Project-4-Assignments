"""
Program: Age Riddle Solver
--------------------------
This program calculates and displays the ages of five friends
based on given conditions.
"""

def main():
    # Assigning ages based on the given conditions
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen  # Ethan's age is the same as Chen's

    # Displaying the results
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

# Ensuring main() runs only when the script is executed directly
if __name__ == '__main__':
    main()
