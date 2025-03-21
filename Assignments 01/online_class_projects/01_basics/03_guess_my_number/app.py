import random

def main():
    # Secret number generate karo
    hidden_number = random.randint(1, 99)
    
    print("I'm thinking of a number between 1 and 99...")

    while True:
        # User se input lo
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        # Guess check karo
        if user_guess < hidden_number:
            print("Too low! Try again.")
        elif user_guess > hidden_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it right: {hidden_number} 🎯")
            break  # Loop exit

if __name__ == "__main__":
    main()
