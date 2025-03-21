""" Get Last Element - By [Your Name] """

def get_last_element(lst):
    """ Last element print karo """
    print("Last element:", lst[-1])  # Directly access last element

def main():
    lst = []
    while (elem := input("Enter an element (or press enter to stop): ")):
        lst.append(elem)

    get_last_element(lst)

if __name__ == '__main__':
    main()
