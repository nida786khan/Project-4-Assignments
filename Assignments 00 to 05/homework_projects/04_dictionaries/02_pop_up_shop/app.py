def calculate_total_cost():
    """Prompts user for quantity of each fruit and calculates total cost."""
    fruits = {
        'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }
    
    total_cost = 0.0
    
    print("\n🛒 Welcome to the Fruit Shop! 🏬")
    
    for fruit, price in fruits.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want to buy?: ").strip())
                if quantity < 0:
                    print("❌ Quantity cannot be negative. Try again.")
                else:
                    total_cost += price * quantity
                    break  # Exit loop if input is valid
            except ValueError:
                print("❌ Invalid input! Please enter a whole number.")

    print(f"\n💰 Your total is **${total_cost:.2f}**")


def main():
    """Main function to execute the fruit shop program."""
    calculate_total_cost()


if __name__ == '__main__':
    main()
