"""
🎲 Dice Roller Simulator 🎲
---------------------------
This program simulates rolling two dice and prints 
the result of each roll along with the total.
"""

import random

NUM_SIDES = 6  # Number of sides on each die

def roll_dice():
    return random.randint(1, NUM_SIDES)

def main():
    print("🎲 Welcome to the Dice Roller Simulator! 🎲\n")

    while True:
        input("Press Enter to roll the dice (or type 'exit' to quit): ").strip().lower()
        
        die1 = roll_dice()
        die2 = roll_dice()
        total = die1 + die2

        print(f"🎲 First die: {die1}")
        print(f"🎲 Second die: {die2}")
        print(f"🎯 Total of two dice: {total}\n")

        choice = input("Roll again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thanks for playing! 🎲 See you next time! 👋")
            break

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
