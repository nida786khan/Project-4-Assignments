import random

NUM_ROUNDS = 5
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("Welcome to the High-Low Game!")
    print("-" * 32)
    
    score = 0  # Player's score

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers
        user_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)

        print(f"Your number is {user_number}")

        # Get user input with validation
        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess in ["higher", "lower"]:
                break
            print("Invalid input! Please enter either 'higher' or 'lower'.")

        # Game logic
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")  # Print score after each round

    # Final message based on performance
    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly! 🎉")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well! 👍")
    else:
        print("Better luck next time! 😢")

if __name__ == '__main__':
    main()
