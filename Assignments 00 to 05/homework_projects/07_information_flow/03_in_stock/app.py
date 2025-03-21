def num_in_stock(fruit: str) -> int:
    """
    Returns the number of the given fruit in stock.
    """
    inventory = {
        "apple": 2,
        "durian": 4,
        "pear": 1000
    }
    
    return inventory.get(fruit.lower(), 0)  # Returns 0 if fruit is not found

def main():
    fruit = input("Enter a fruit: ").strip()  # Remove extra spaces
    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
