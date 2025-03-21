"""
🎭 Fun Mad Libs Game 🎭
--------------------------------
This program prompts the user for an adjective, a noun, and a verb,
then constructs a funny sentence using their inputs!
"""

import random

# List of possible sentence starters for extra fun!
SENTENCE_STARTS = [
    "Panaversity is fun. I learned to program and used Python to make my",
    "Coding is an adventure! Today, I saw a",
    "Once upon a time, a",
    "In a mysterious land, there lived a"
]

def main():
    # Get the three inputs from the user
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Pick a random sentence starter
    sentence_start = random.choice(SENTENCE_STARTS)

    # Construct the funny sentence
    print(f"{sentence_start} {adjective} {noun} {verb}!")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
