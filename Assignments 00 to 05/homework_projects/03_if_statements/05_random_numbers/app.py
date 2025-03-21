import random

N_NUMBERS = 10  # Number of random values
MIN_VALUE = 1   # Minimum range
MAX_VALUE = 100 # Maximum range

def main():
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(" ".join(map(str, random_numbers)))  # Convert list to string & print

if __name__ == '__main__':
    main()
