import sys
import json

with (open('organizations.json', 'r')) as openfile:
    organizations = json.load(openfile)


def print_info():
    print(f'''
Organization:
    {selected_organization.get('name')} ({selected_organization.get('id')})
    Adress: {selected_organization.get('adress')},
    Contacts:''')
    for contact in selected_organization.get('contacts'):
        print(f"        {contact.get('name')} ({contact.get('position')}) ID: {contact.get('id')}")
    print('_' * 50)


def add_contact():
    name = input('Name: ')
    position = input('Position: ')
    id = int(input('ID: '))
    selected_organization.get('contacts').append({
        'name': name,
        'position': position,
        'id': id
    })


def add_organization():
    name = input('Name: ')
    address = input('Adress: ')
    id = input('ID: ')
    org = {
        'name': name,
        'adress': address,
        'id': id,
        'contacts': []
    }
    organizations.append(org)


def select_organization():
    if len(organizations) != 0:
        for i in range(len(organizations)):
            print(f"{i} - {organizations[i].get('name')}")
        while True:
            selected_organization_num = int(input("Enter number of organization: "))
            try:
                global selected_organization
                selected_organization = organizations[selected_organization_num]
            except:
                print("Invalid number")
            else:
                break
    else:
        print('There are no organizations yet')


def stop_running():
    sys.exit()


def reset_select():
    global selected_organization
    selected_organization = None


def delete_organization():
    if len(organizations) != 0:
        for i in range(len(organizations)):
            print(f"{i} - {organizations[i].get('name')}")
        while True:
            organization_to_del_num = int(input("Enter number of organization to delete: "))
            confirm = input('Are you sure?[Y/N upper case] ')
            if confirm == 'Y':
                try:
                    deleted_organization = organizations.pop(organization_to_del_num)
                except:
                    print("Invalid number")
                else:
                    print(f"{deleted_organization.get('name')} HAS BEEN DELETED")
                    break
            else:
                break
    else:
        print('There are no organizations yet')


def delete_contact():
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
                except:
                    print("Invalid number")
                else:
                    print(
                        f"{deleted_contact.get('name')} ({deleted_contact.get('position')}) ID: {deleted_contact.get('id')} HAS BEEN DELETED")
                    break
            else:
                break
    else:
        print('There are no contacts yet')


def main():
    while True:
        if selected_organization:
            print(f'Selected: {selected_organization.get("name")}')
            response = input('Add contact - 1\n'
                             'Delete contact - D\n'
                             'Organization info - 2\n'
                             'Back - B\n').lower()
            activities = {'1': add_contact,
                          '2': print_info,
                          'b': reset_select,
                          'd': delete_contact}

        else:
            response = input('Add organization - 1\n'
                             'Select organizatoin - 2\n'
                             'Delete organiztion - D\n'
                             'Exit - E\n').lower()
            activities = {'1': add_organization,
                          '2': select_organization,
                          'e': stop_running,
                          'd': delete_organization}

        activities.get(response, lambda: print('Invalid response'))()

        with (open('organizations.json', 'w')) as outfile:
            json.dump(organizations, outfile, indent=4)
        print('\n' + '*' * 30 + '\n')


if __name__ == '__main__':
    selected_organization = None
    main()
