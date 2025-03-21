AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    while True:
        user_input = input(f"Please type the following affirmation: {AFFIRMATION}\n")
        if user_input == AFFIRMATION:
            print("That's right! 😊")
            break  # Exit loop when correct affirmation is typed
        print("Hmmm... That was not the affirmation. Try again!\n")

if __name__ == "__main__":
    main()
