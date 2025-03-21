# Constants
PROMPT: str = "What would you like? "
JOKE: str = "Here is a joke for you! 🚀 Why do programmers prefer dark mode? Because light attracts bugs! 😂"
SORRY: str = "Sorry, I only tell jokes."

def main():
    # Asking user input
    user_input = input(PROMPT).strip().lower()

    # Checking input and responding
    if user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)

# Running the program
if __name__ == "__main__":
    main()
