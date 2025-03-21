""" Shorten List Program - By [Your Name] """

MAX_LENGTH = 3  # Maximum length fix kar diya

def shorten(lst):
    """ List ko shorten karne ka function """
    while len(lst) > MAX_LENGTH:
        print(lst.pop())  # Last element hatao aur print karo

def get_lst():
    """ User se input lekar ek list generate karo """
    lst = []
    while (elem := input("Enter an element (press enter to stop): ")):  
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()
