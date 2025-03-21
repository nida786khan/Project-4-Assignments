def is_odd(value: int):
    """
    Returns True if the number is odd, otherwise False.
    """
    return value % 2 == 1

def main():
    for i in range(10, 20):  # 10 se 19 tak ke numbers ke liye loop
        if is_odd(i):
            print(i, "odd")  # Agar odd hai toh 'odd' print karega
        else:
            print(i, "even")  # Agar even hai toh 'even' print karega

if __name__ == '__main__':
    main()
