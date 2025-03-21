""" Mutable vs Immutable - By [Your Name] """

def add_three_copies(my_list, data):
    """ List me 3 baar data add karo (mutability proof!) """
    my_list += [data] * 3

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()
