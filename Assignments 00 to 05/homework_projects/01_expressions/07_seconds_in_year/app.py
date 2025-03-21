"""
📆 Calculate Seconds in a Year 📆
---------------------------------
This program calculates the total number of seconds in 
a normal year (365 days) and a leap year (366 days).
"""

# Constants for time conversion
DAYS_PER_YEAR = 365
DAYS_PER_LEAP_YEAR = 366
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def calculate_seconds(days: int) -> int:
    """Calculates the total number of seconds in a given number of days."""
    return days * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

def main():
    print("📆 Welcome to the Yearly Seconds Calculator! 📆\n")

    normal_year_seconds = calculate_seconds(DAYS_PER_YEAR)
    leap_year_seconds = calculate_seconds(DAYS_PER_LEAP_YEAR)

    print(f"There are {normal_year_seconds} seconds in a normal year (365 days).")
    print(f"There are {leap_year_seconds} seconds in a leap year (366 days).")

    # Let the user input a year to check if it's a leap year
    year = int(input("\nEnter a year to check its total seconds: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year! It has {leap_year_seconds} seconds.")
    else:
        print(f"{year} is a normal year! It has {normal_year_seconds} seconds.")

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
