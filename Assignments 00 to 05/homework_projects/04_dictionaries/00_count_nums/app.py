def get_user_numbers():
    """Collects numbers from the user until they enter a blank line."""
    user_numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":  # Stop when user enters blank input
            break
        user_numbers.append(int(user_input))  # Convert to int and store
    return user_numbers

def count_nums(num_list):
    """Counts occurrences of numbers using a dictionary."""
    num_counts = {}
    for num in num_list:
        num_counts[num] = num_counts.get(num, 0) + 1  # Increment count
    return num_counts

def print_counts(num_counts):
    """Prints the count of each number."""
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

def main():
    """Runs the number counting program."""
    user_numbers = get_user_numbers()
    num_counts = count_nums(user_numbers)
    print_counts(num_counts)

if __name__ == '__main__':
    main()
