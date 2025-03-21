def print_ones_digit(num: int):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10
    print(f"The last digit of {num} is {ones_digit}.")

def main():
    try:
        num = int(input("Enter a number: "))
        print_ones_digit(num)
    except ValueError:
        print("Oops! Please enter a valid integer.")

if __name__ == '__main__':
    main()
