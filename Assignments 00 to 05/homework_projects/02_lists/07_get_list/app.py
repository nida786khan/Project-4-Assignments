""" Collect and Display List - By [Your Name] """

def main():
    lst = []  # Empty list banaya store karne ke liye

    while (val := input("Enter a value (press enter to stop): ")):  # Jab tak user kuch daalta rahe
        lst.append(val)  # List mein add kar do

    print("Here's the list:", lst)  # Final list print karo

if __name__ == '__main__':
    main()
