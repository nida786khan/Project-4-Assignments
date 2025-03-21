"""
🔢 Sum of Numbers Program 🔢
--------------------------------
This program takes a list of numbers and returns their sum.
The user can either input their own numbers or use a default list.
"""

def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes a list of numbers and returns their sum.
    """
    return sum(numbers)  # Using built-in sum function for simplicity

def main():
    # Asking user if they want to enter numbers manually
    choice = input("Do you want to enter numbers? (yes/no): ").strip().lower()

    if choice == "yes":
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, user_input.split()))  # Convert input to a list of integers
    else:
        numbers = [1, 2, 3, 4, 5]  # Default list of numbers

    sum_of_numbers = add_many_numbers(numbers)  # Calculate sum
    print(f"The sum of {numbers} is {sum_of_numbers}.")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
