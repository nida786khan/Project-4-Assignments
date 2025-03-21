MAX_TERM_VALUE = 10000  # Maximum value for Fibonacci terms

def main():
    curr_term, next_term = 0, 1  # Initial Fibonacci numbers
    fibonacci_sequence = []  # List to store Fibonacci numbers

    while curr_term <= MAX_TERM_VALUE:
        fibonacci_sequence.append(curr_term)
        curr_term, next_term = next_term, curr_term + next_term  # Swap and update terms

    print(" ".join(map(str, fibonacci_sequence)))  # Print all terms in one line

if __name__ == '__main__':
    main()
