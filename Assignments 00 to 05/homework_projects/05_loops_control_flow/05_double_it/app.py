def main():
    curr_value = int(input("Enter a number: "))  # User se input le rahe hain

    while curr_value < 100:  # Jab tak value 100 se chhoti hai, loop chalega
        curr_value *= 2  # Value ko double kar rahe hain
        print(curr_value, end=" ")  # Ek line mein space ke sath print karenge

if __name__ == "__main__":
    main()
