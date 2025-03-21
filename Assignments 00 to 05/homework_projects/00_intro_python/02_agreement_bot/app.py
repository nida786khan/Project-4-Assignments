"""
Program: Favorite Animal
------------------------
This program asks the user about their favorite animal 
and responds with the same choice.
"""

def main():
    # Asking user for their favorite animal
    favorite_animal = input("What's your favorite animal? ").strip()

    # Displaying response
    print(f"My favorite animal is also {favorite_animal}!")

# Ensuring main() runs only when the script is executed directly
if __name__ == '__main__':
    main()
