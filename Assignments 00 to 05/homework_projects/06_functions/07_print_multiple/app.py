def print_multiple(message: str, repeats: int):
    """
    Prints the given message the specified number of times.
    """
    print((message + "\n") * repeats, end="")  # String multiplication se ek hi line me sab print kar diya

def main():
    message = input("Please type a message: ")  # User se message lena hai
    repeats = int(input("Enter a number of times to repeat your message: "))  # Kitni baar repeat karna hai
    print_multiple(message, repeats)  # Function call kar diya

if __name__ == '__main__':
    main()
