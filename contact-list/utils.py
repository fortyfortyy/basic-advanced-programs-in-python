def verify_phone_number(phone_number):
    phone_number = phone_number.replace("-", "")

    for digit in phone_number:
        if not digit.isdigit():
            return False

    return len(phone_number) == 9


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def get_contact_by_name(first_name, last_name, contacts, to_delete=None):
    for contact in contacts:
        contact_first_name = contact['first_name']
        contact_last_name = contact['last_name']
        if first_name == contact_first_name and last_name == contact_last_name:
            if to_delete:
                return contact
            return False   # contact with first and last name already exists so can't be added to the contact list

    if to_delete:
        return False
    return True


def validate_inputs(contacts, **input_names):
    for input_name in input_names:
        if input_name == 'first_name':
            first_name = input_names[input_name]
            if first_name.isdigit() or len(first_name) < 3:
                return False, 'Invalid first name.'

        elif input_name == 'last_name':
            last_name = input_names[input_name]
            if last_name.isdigit() or len(last_name) < 3:
                return False, 'Invalid last name.'

        elif input_name == 'mobile_phone':
            mobile_phone = input_names[input_name]
            if len(mobile_phone) > 0:
                result = verify_phone_number(mobile_phone)
                if not result:
                    return False, 'Invalid home phone.'

        elif input_name == 'home_phone':
            home_phone = input_names[input_name]
            if len(home_phone) > 0:
                result = verify_phone_number(home_phone)
                if not result:
                    return False, 'Invalid home phone.'

        elif input_name == 'email':
            email = input_names[input_name]
            if len(email) > 0:
                result = verify_email_address(email)
                if not result:
                    return False, 'Invalid email address.'

    # check if contact with first and last name already exists
    first_name = input_names['first_name']
    last_name = input_names['last_name']
    result = get_contact_by_name(first_name, last_name, contacts)
    if not result:
        return False, 'A contact with this name already exists.'

    return True, ''

