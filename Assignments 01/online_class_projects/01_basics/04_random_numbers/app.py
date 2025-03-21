import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Prints 10 random numbers in the range 1 to 100.
    """
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(" ".join(map(str, random_numbers)))  # Joining numbers with spaces

if __name__ == '__main__':
    main()
