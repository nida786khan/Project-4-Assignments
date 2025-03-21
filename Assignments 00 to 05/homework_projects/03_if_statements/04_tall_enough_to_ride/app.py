MINIMUM_HEIGHT = 50  # Height requirement for the ride

def main():
    while True:
        height_input = input("How tall are you? (Press Enter to exit) ")
        
        if height_input == "":  # Exit condition
            print("Goodbye! Come back when you're ready. 😊")
            break

        try:
            height = float(height_input)  # Convert input to float
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride! 🎢")
            else:
                print("You're not tall enough to ride, but maybe next year! 😊")
        except ValueError:
            print("Please enter a valid number for height!")

if __name__ == '__main__':
    main()
