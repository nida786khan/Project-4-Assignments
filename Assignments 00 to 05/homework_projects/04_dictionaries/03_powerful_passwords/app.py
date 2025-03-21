from hashlib import sha256

def hash_password(password):
    """
    Takes a password and returns its SHA256 hash.
    """
    return sha256(password.encode()).hexdigest()


def login(email, stored_logins, password_to_check):
    """
    Verifies if the entered password (hashed) matches the stored hash for the given email.
    """
    if email not in stored_logins:
        print("❌ Email not found!")
        return False

    if stored_logins[email] == hash_password(password_to_check):
        print("✅ Login successful!")
        return True
    else:
        print("❌ Incorrect password!")
        return False


def main():
    """
    Main function to test login authentication with secure hashing.
    """
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }
    
    # Testing various login attempts
    login("example@gmail.com", stored_logins, "word")  # ❌ Incorrect password!
    login("example@gmail.com", stored_logins, "password")  # ✅ Login successful!
    
    login("code_in_placer@cip.org", stored_logins, "Karel")  # ✅ Login successful!
    login("code_in_placer@cip.org", stored_logins, "karel")  # ❌ Incorrect password!
    
    login("student@stanford.edu", stored_logins, "password")  # ❌ Incorrect password!
    login("student@stanford.edu", stored_logins, "123!456?789")  # ✅ Login successful!

    login("unknown@domain.com", stored_logins, "randompass")  # ❌ Email not found!


if __name__ == '__main__':
    main()
