def print_divisors(num: int):
    """
    Prints all divisors of a given number.
    """
    print(f"Here are the divisors of {num}: ", end="")  
    divisors = [i for i in range(1, num + 1) if num % i == 0]  # List comprehension se divisors find kar rahe hain
    print(*divisors)  # List ko space-separated format me print kar diya

def main():
    num = int(input("Enter a number: "))  # User se ek number lena hai
    print_divisors(num)  # Function ko call karna hai

if __name__ == '__main__':
    main()
