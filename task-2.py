class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            print("Search Results:")
            for contact in results:
                print(contact)

    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def user_interface():
    book = ContactBook()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)

        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            book.search_contact(search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            address = input("Enter new address (or press Enter to skip): ")
            book.update_contact(name, phone if phone else None, email if email else None, address if address else None)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    user_interface()

