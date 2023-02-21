import sys
import json

'''Loads organizations from file'''
with (open('organizations.json', 'r')) as openfile:
    organizations = json.load(openfile)


def select_organization():
    """Selects organizations"""
    if len(organizations) != 0:
        for i in range(len(organizations)):
            print(f"{i} - {organizations[i].get('name')}")

        while True:
            try:
                selected_organization_num = int(input("Enter number of organization: "))
                global selected_organization
                selected_organization = organizations[selected_organization_num]
            except (IndexError, ValueError):
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
            try:
                contact_to_del_num = int(input("Enter number of contact to delete: "))
                contacts[contact_to_del_num]
            except (IndexError, ValueError):
                print("Invalid number")
            else:
                confirm = input('\nAre you sure?[Y/N upper case]')
                if confirm == 'Y':
                    deleted_contact = selected_organization.get('contacts').pop(contact_to_del_num)
                    print(
                            f"{deleted_contact.get('name')} ({deleted_contact.get('position')}) ID: {deleted_contact.get('id')} HAS BEEN DELETED")
                break
    else:
        print('There are no contacts yet')


def reset_selection():
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
            try:
                organization_to_del_num = int(input("Enter number of organization to delete: "))
                organizations[organization_to_del_num]
            except (IndexError, ValueError):
                print("Invalid number")
            else:
                confirm = input('\nAre you sure?[Y/N upper case]')
                if confirm == 'Y':
                    deleted_organization = organizations.pop(organization_to_del_num)
                    print(f"{deleted_organization.get('name')} HAS BEEN DELETED")
                break
    else:
        print('There are no organizations yet')


def edit_income():
    income = int(input("Income: "))
    selected_organization["income"] = income


def print_income_top():
    sorted_orgs = list(reversed(sorted(organizations, key=lambda d: d['income'])))
    for index, company in enumerate(sorted_orgs[:5]):
        print(f"{index + 1} - {company.get('name')} ({company.get('income')}$)")


def get_organization_by_id():
    id_list = [org.get('id') for org in organizations]
    while True:
        org_id = input("ID: ")
        try:
            index = id_list.index(org_id)
        except ValueError:
            print('No such ID')
        else:
            global selected_organization
            selected_organization = organizations[index]
            break


def main():
    while True:
        if selected_organization:
            print(f'Selected: {selected_organization.get("name")}')
            response = input('Add contact - A\n'
                             'Delete contact - D\n'
                             'Organization info - I\n'
                             'Edit income - E\n'
                             'Back - B\n').lower()
            activities = {'a': add_contact,
                          'd': delete_contact,
                          'i': print_info,
                          'e': edit_income,
                          'b': reset_selection}

        else:
            response = input('Add organization - A\n'
                             'Delete organization - D\n'
                             'Select organization - S\n'
                             'Get TOP 5 income companies - T\n'
                             'Find organization by ID - F\n'
                             'Exit - E\n').lower()
            activities = {'a': add_organization,
                          'd': delete_organization,
                          's': select_organization,
                          't': print_income_top,
                          'f': get_organization_by_id,
                          'e': lambda: sys.exit()}

        activities.get(response, lambda: print('Invalid response'))()

        with (open('organizations.json', 'w')) as outfile:
            json.dump(organizations, outfile, indent=4)
        print('\n' + '*' * 30 + '\n')


if __name__ == '__main__':
    selected_organization = None
    main()
