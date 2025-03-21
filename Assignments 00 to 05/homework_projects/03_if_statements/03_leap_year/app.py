def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    year = int(input("Please input a year: "))
    print("That's a leap year!" if is_leap_year(year) else "That's not a leap year.")

if __name__ == '__main__':
    main()
