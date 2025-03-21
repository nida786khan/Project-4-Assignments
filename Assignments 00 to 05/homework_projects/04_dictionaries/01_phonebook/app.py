def create_phonebook():
    """Takes user input to create a phonebook dictionary."""
    contacts = {}  
    
    while True:
        person = input("Enter name (or press Enter to stop): ").strip()
        if not person:
            break
        phone = input(f"Enter phone number for {person}: ").strip()
        contacts[person] = phone  # Store name-number pair
    
    return contacts

def display_contacts(contacts):
    """Displays all saved contacts."""
    if not contacts:
        print("📭 Your phonebook is empty!")
        return
    print("\n📖 Phonebook List:")
    for person, phone in contacts.items():
        print(f"{person}: {phone}")

def search_contact(contacts):
    """Allows users to search for a contact."""
    while True:
        search_name = input("\nEnter name to search (or press Enter to exit): ").strip()
        if not search_name:
            break
        print(contacts.get(search_name, f"{search_name} not found in phonebook."))

def main():
    """Main function to execute the phonebook program."""
    phonebook = create_phonebook()
    display_contacts(phonebook)
    search_contact(phonebook)

if __name__ == "__main__":
    main()
