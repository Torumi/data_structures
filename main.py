import sys
import json

'''Load organizations'''
with (open('organizations.json', 'r')) as openfile:
    organizations = json.load(openfile)


def select_organization():
    """Selects organizations"""
    if len(organizations) != 0:
        for i in range(len(organizations)):
            print(f"{i} - {organizations[i].get('name')}")
        while True:
            selected_organization_num = int(input("Enter number of organization: "))
            try:
                global selected_organization
                selected_organization = organizations[selected_organization_num]
            except IndexError:
                print("Invalid number")
            else:
                break
    else:
        print('There are no organizations yet')


def print_info():
    """Prints info about selected organization"""
    print(f'''
Organization:
    {selected_organization.get('name')} ({selected_organization.get('id')})
    Adress: {selected_organization.get('adress')},
    Income: {selected_organization.get('income')}$
    Contacts:''')
    for contact in selected_organization.get('contacts'):
        print(f"        {contact.get('name')} ({contact.get('position')}) ID: {contact.get('id')}")
    print('_' * 50)


def add_contact():
    """Adds a contact to selected organization"""
    name = input('Name: ')
    position = input('Position: ')
    contact_id = int(input('ID: '))
    selected_organization.get('contacts').append({
        'name': name,
        'position': position,
        'id': contact_id
    })


def delete_contact():
    """Deletes a contact of selected organization"""
    contacts = selected_organization.get('contacts')
    if len(contacts) != 0:
        for i in range(len(contacts)):
            print(f"{i} - {contacts[i].get('name')} ({contacts[i].get('position')}) ID: {contacts[i].get('id')}")
        while True:
            contact_to_del_num = int(input("Enter number of contact to delete: "))
            confirm = input('\nAre you sure?[Y/N upper case]')
            if confirm == 'Y':
                try:
                    deleted_contact = selected_organization.get('contacts').pop(contact_to_del_num)
                except IndexError:
                    print("Invalid number")
                else:
                    print(
                        f"{deleted_contact.get('name')} ({deleted_contact.get('position')}) ID: {deleted_contact.get('id')} HAS BEEN DELETED")
                    break
            else:
                break
    else:
        print('There are no contacts yet')


def reset_select():
    """Resets selection of organization"""
    global selected_organization
    selected_organization = None


def add_organization():
    """Adds organization to list"""
    name = input('Name: ')
    address = input('Adress: ')
    organization_id = input('ID: ')
    org = {
        'name': name,
        'adress': address,
        'id': organization_id,
        'contacts': [],
        'income': 0
    }
    organizations.append(org)


def delete_organization():
    """Delete organization from list"""
    if len(organizations) != 0:
        for i in range(len(organizations)):
            print(f"{i} - {organizations[i].get('name')}")
        while True:
            organization_to_del_num = int(input("Enter number of organization to delete: "))
            confirm = input('Are you sure?[Y/N upper case] ')
            if confirm == 'Y':
                try:
                    deleted_organization = organizations.pop(organization_to_del_num)
                except IndexError:
                    print("Invalid number")
                else:
                    print(f"{deleted_organization.get('name')} HAS BEEN DELETED")
                    break
            else:
                break
    else:
        print('There are no organizations yet')

def add_income():
    income = int(input("Income: "))
    selected_organization["income"] = income

def print_income_top():
    sorted_orgs = list(reversed(sorted(organizations, key=lambda d: d['income'])))
    for index, company in enumerate(sorted_orgs[:5]):
        print(f"{index+1} - {company.get('name')} ({company.get('income')}$)")

def get_organization_by_id():
    ID = input("ID: ")
    for organization in organizations:
        if organization.get('id') == ID:
            global selected_organization
            selected_organization = organization

def main():
    while True:
        if selected_organization:
            print(f'Selected: {selected_organization.get("name")}')
            response = input('Add contact - 1\n'
                             'Delete contact - D\n'
                             'Organization info - 2\n'
                             'Back - B\n'
                             'Add income - I\n').lower()
            activities = {'1': add_contact,
                          '2': print_info,
                          'b': reset_select,
                          'd': delete_contact,
                          'i': add_income}

        else:
            response = input('Add organization - 1\n'
                             'Select organization - 2\n'
                             'Delete organization - D\n'
                             'Exit - E\n'
                             'Get top 5 income companies - I\n'
                             'Find organization by ID - F\n').lower()
            activities = {'1': add_organization,
                          '2': select_organization,
                          'e': lambda: sys.exit(),
                          'd': delete_organization,
                          'i': print_income_top,
                          'f': get_organization_by_id}

        activities.get(response, lambda: print('Invalid response'))()

        with (open('organizations.json', 'w')) as outfile:
            json.dump(organizations, outfile, indent=4)
        print('\n' + '*' * 30 + '\n')


if __name__ == '__main__':
    selected_organization = None
    main()
