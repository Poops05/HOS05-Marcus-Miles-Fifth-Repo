from contact_book import add_contact, remove_contact, search_contact, list_contacts
from display import display_message, display_contacts


def main():
    contacts = {}

    contacts = add_contact(contacts, "John Doe", "123-456-7890")
    contacts = add_contact(contacts, "Jane Doe", "987-654-3210")

    display_contacts(contacts)

    message = search_contact(contacts, "John Doe")
    display_message(message)

    contacts = remove_contact(contacts, "John Doe")
    display_contacts(contacts)

if __name__ == "__main__":
    main()
