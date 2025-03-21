def get_user_info():
    """
    Collects user data: first name, last name, and email.
    Returns the data as a tuple.
    """
    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    email_address = input("What is your email address?: ").strip()
    
    return first_name, last_name, email_address  # Returning as a tuple

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
