ADULT_AGE = 18  # Minimum age to be considered an adult in the U.S.

def is_adult(age: int) -> bool:
    """
    Checks if the given age qualifies as an adult age.
    Returns True if age >= ADULT_AGE, otherwise False.
    """
    return age >= ADULT_AGE

def main():
    try:
        age = int(input("Please enter the person's age: "))
        result = "Yes, an adult." if is_adult(age) else "No, not an adult."
        print(result)
    except ValueError:
        print("Invalid input! Please enter a valid integer age.")

if __name__ == '__main__':
    main()
