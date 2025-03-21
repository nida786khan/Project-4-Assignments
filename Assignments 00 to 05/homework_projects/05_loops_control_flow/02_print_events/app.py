def main():
    even_numbers = [i * 2 for i in range(20)]  # List comprehension for 20 even numbers
    print(" ".join(map(str, even_numbers)))  # Print in a single line

if __name__ == "__main__":
    main()
