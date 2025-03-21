def double(num: int):
    """
    Returns double the given number.
    >>> double(2)
    4
    >>> double(5)
    10
    """
    return num * 2

def main():
    num = int(input("Enter a number: "))  
    num_times_2 = double(num)  
    print("Double that is", num_times_2)  

if __name__ == '__main__':
    main()
