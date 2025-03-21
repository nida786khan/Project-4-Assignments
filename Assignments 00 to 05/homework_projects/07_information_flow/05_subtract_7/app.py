def subtract_seven(num: int) -> int:
    """
    Subtracts 7 from the given number.
    """
    return num - 7  # Directly returning the result

def main():
    num = 7  # Initial number
    num = subtract_seven(num)  # Calling the helper function
    print("This should be zero:", num)

if __name__ == "__main__":
    main()
