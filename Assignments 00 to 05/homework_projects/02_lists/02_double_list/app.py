"""
🔢 Double Each Element Program 🔢
---------------------------------
This program doubles each element in a list of numbers.
The user can enter their own list or use the default list.
"""

def double_numbers(numbers: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns a new list with each number doubled.
    """
    return [num * 2 for num in numbers]  # Using list comprehension for simplicity

def main():
    # Asking user if they want to enter numbers manually
    choice = input("Do you want to enter numbers? (yes/no): ").strip().lower()

    if choice == "yes":
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, user_input.split()))  # Convert input to a list of integers
    else:
        numbers = [1, 2, 3, 4]  # Default list of numbers

    doubled_numbers = double_numbers(numbers)  # Double each number
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_numbers}")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
