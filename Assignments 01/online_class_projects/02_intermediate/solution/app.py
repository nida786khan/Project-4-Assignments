import random

NUM_ROUNDS = 5

def play_round(round_num, score):
    print(f"Round {round_num}")
    player_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)
    print(f"Your number is {player_num}")
    
    # Get a valid user choice
    while True:
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        if guess in ["higher", "lower"]:
            break
        print("Invalid input. Please enter 'higher' or 'lower'.")
    
    # Check if the player's guess is correct
    if (guess == "higher" and player_num > computer_num) or (guess == "lower" and player_num < computer_num):
        print(f"Correct! The computer's number was {computer_num}.")
        score += 1
    else:
        print(f"Incorrect. The computer's number was {computer_num}.")
    
    print(f"Your score is now {score}\n")
    return score

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0
    
    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)
    
    print("Game Over!")
    print(f"Final Score: {score}")
    
    if score == NUM_ROUNDS:
        print("Amazing! You got everything right!")
    elif score >= NUM_ROUNDS // 2:
        print("Great job! You did well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
