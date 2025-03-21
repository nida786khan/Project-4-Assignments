"""
Program: Dice Rolling Simulator 🎲
---------------------------------
This program simulates rolling two dice three times.
It also demonstrates the concept of variable scope in Python.
"""

import random  # Importing the random module

# Define a constant for the number of sides on a die
NUM_SIDES = 6  

def roll_two_dice():
    """
    Simulates rolling two dice and prints the values along with the total.
    """
    die_one = random.randint(1, NUM_SIDES)  # Roll first die
    die_two = random.randint(1, NUM_SIDES)  # Roll second die
    total = die_one + die_two  # Calculate sum of both dice

    print(f"🎲 Die 1: {die_one}, 🎲 Die 2: {die_two} → Total: {total}")

def main():
    local_die = 10  # Local variable inside main()
    print(f"🔹 Variable in main() starts as: {local_die}\n")

    # Rolling dice three times using a loop
    for roll_number in range(1, 4):
        print(f"🔄 Roll {roll_number}:")
        roll_two_dice()
        print("-" * 25)

    print(f"\n🔹 Variable in main() remains: {local_die}")

# Ensures the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()
