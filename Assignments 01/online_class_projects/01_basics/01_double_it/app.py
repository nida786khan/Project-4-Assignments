def main():
    # User se number lena
    num = int(input("Enter a number: "))

    # Current value ko user ke number se initialize karna
    current_value = num

    # Jab tak value 100 se chhoti hai, tab tak double karna
    while current_value < 100:
        current_value *= 2
        print(current_value, end=" ")

# Program start karne ke liye zaroori line
if __name__ == "__main__":
    main()
