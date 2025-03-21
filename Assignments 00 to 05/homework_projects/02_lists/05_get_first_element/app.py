""" Get First Element - By [Your Name] """

def get_first_element(lst):
    """ Pehla element print karo """
    print("First element:", lst[0])

def main():
    lst = []
    while (elem := input("Enter an element (or press enter to stop): ")):
        lst.append(elem)

    get_first_element(lst)

if __name__ == '__main__':
    main()
