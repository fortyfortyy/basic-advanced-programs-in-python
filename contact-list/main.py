from utils import validate_inputs, get_contact_by_name
from storage import read_contacts, write_contacts

CONTACT_FILE_PATH = 'contacts.json'


def get_user_command():
    while True:
        command = input('Type a command: ').lower().strip()

        if command.isdigit() or command not in ['add', 'delete', 'list', 'search', 'q']:
            print('Unknown command.')
            continue
        break

    return command


def add_contact(contacts):
    first_name = input('First Name: ').lower()
    last_name = input('Last Name: ').lower()
    mobile_phone = input('Mobile Phone Number: ')
    home_phone = input('Home Phone Number: ')
    email = input('Email Address: ').lower()
    address = input('Address: ').lower()
    result, message = validate_inputs(
        contacts,
        **{'first_name': first_name, 'last_name': last_name, 'mobile_phone': mobile_phone,
           'home_phone': home_phone, 'email': email}
    )
    if not result:
        print(message)
        print('You entered invalid information, this contact was not added.')
        return False

    new_contact = {
        'first_name': first_name,
        'last_name': last_name,
        'mobile_phone': mobile_phone,
        'home_phone': home_phone,
        'email': email,
        'address': address,
    }

    contacts.append(new_contact)
    return True


def search_for_contact(contacts):
    first_name_search_string = input("First Name: ").lower().strip()
    last_name_search_string = input("Last Name: ").lower().strip()

    matching_contacts = list(filter(lambda contact:
                                    (first_name_search_string and first_name_search_string in contact['first_name']) or
                                    (last_name_search_string and last_name_search_string in contact['last_name']),
                                    contacts))

    print(f"Found {len(matching_contacts)} matching contacts.")
    list_contacts(matching_contacts)


def delete_contact(contacts):
    first_name = input("First Name: ").lower().strip()
    last_name = input("Last Name: ").lower().strip()

    contact = get_contact_by_name(first_name, last_name, contacts, to_delete=True)
    if not contact:
        print("No contact with this name exists.")
    else:
        confirm = input("Are you sure you would like to delete this contact (y/n)? ").lower()
        if confirm in ["y", "yes"]:
            contacts.remove(contact)
            print("Contact deleted!")


def list_contacts(contacts):
    if len(contacts) == 0:
        print('You dont have any contacts.')

    for idx, contact in enumerate(contacts):
        string = f"{idx + 1}. {contact['first_name'].title()} {contact['last_name'].title()}"

        if contact['mobile_phone']:
            string += f"\n   Mobile: {contact['mobile_phone']}"
        if contact['home_phone']:
            string += f"\n   Home phone: {contact['home_phone']}"
        if contact['email']:
            string += f"\n   Email: {contact['email']}"
        if contact['address']:
            string += f"\n   Address: {contact['address'].title()}"

        print(string)


def main(contacts_path):
    print('\nWelcome to your contact list! \n'
          'The following is a list of useable commands:'
          '\n')

    print('"add": Adds a contact. \n'
          '"delete": Deletes a contact. \n'
          '"list": Lists all contacts. \n'
          '"search": Searches for a contact by name. \n'
          '"q": Quits the program and saves the contact list.'
          '\n')

    contacts = read_contacts(contacts_path)

    while True:
        chosen_command = get_user_command()

        if chosen_command == 'add':
            result = add_contact(contacts)
            if result:
                print('Contact Added!')
                write_contacts(contacts_path, contacts)

        elif chosen_command == 'delete':
            delete_contact(contacts)
        elif chosen_command == 'list':
            list_contacts(contacts)
        elif chosen_command == 'search':
            search_for_contact(contacts)
        else:
            write_contacts(contacts_path, contacts)
            print('Contacts were saved successfully.')
            break


if __name__ == '__main__':
    main(CONTACT_FILE_PATH)
