def greet(name: str) -> None:
    """
    Prints a personalized greeting message.
    """
    print(f"Hello, {name}! Hope you’re having a great day! 😊")

def main():
    user_name = input("Please enter your name: ").strip()
    if user_name:  # Ensuring input is not empty
        greet(user_name)
    else:
        print("Oops! You didn't enter a name.")

if __name__ == '__main__':
    main()
