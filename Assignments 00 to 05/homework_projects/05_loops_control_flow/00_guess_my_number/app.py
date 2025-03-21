import random

def main():
    # Randomly select a number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("\n🎯 I am thinking of a number between 1 and 99...")
    attempts = 0  # Counter for the number of attempts

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 99:
                print("⚠️ Please enter a number between 1 and 99.")
                continue  # Skip the rest of the loop and ask for input again

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congrats! The number was {secret_number} 🎯")
                print(f"🏆 You guessed it in {attempts} attempts!")
                break  # Exit loop when correct number is guessed

        except ValueError:
            print("❌ Invalid input! Please enter a number.")

if __name__ == '__main__':
    main()
