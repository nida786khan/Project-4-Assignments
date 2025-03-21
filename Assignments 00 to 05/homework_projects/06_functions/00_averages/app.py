def average(a: float, b: float) -> float:
    """Returns the number which is halfway between a and b"""
    return (a + b) / 2  # Directly return the average

def main():
    num1 = float(input("Enter first number: "))  # User se pehla number lo
    num2 = float(input("Enter second number: "))  # Dusra number lo
    
    avg = average(num1, num2)  # Function ko call karke average nikalo
    print(f"The average of {num1} and {num2} is: {avg}")  # Result print karo

if __name__ == '__main__':
    main()
