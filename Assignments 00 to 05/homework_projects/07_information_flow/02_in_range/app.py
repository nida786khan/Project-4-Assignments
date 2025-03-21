def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high (inclusive).
    Assumes high > low.
    """
    return low <= n <= high  # Short and Pythonic way

def main():
    num = int(input("Enter a number: "))
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound (greater than lower bound): "))

    if lower >= upper:
        print("Invalid range! The upper bound must be greater than the lower bound.")
    else:
        print(in_range(num, lower, upper))

if __name__ == '__main__':
    main()
