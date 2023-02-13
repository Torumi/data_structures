import sys
import json

organizations = [
    {
        'name': 'Tesla Motors',
        'adress': 'Tesla ave 1, USA',
        'id': '8646678',
        'contacts': [
            {
                'name': 'Elon',
                'position': 'CEO',
                'id': 1
            },
            {
                'name': 'Jenifer',
                'position': 'CTO',
                'id': 2
            }
        ]
    },
    {
        'name': 'Apple',
        'adress': 'Apple Inc., 1 Infinite Loop, Cupertino, CA 95014, USA.',
        'id': '942404110',
        'contacts': [
            {
                'name': 'Tim',
                'position': 'CEO',
                'id': 1
            },
            {
                'name': 'Steve',
                'position': 'CTO',
                'id': 2
            }
        ]
    }
]



def print_info():
    organization = get_organization(selected_organization)
    print(f'''
Organization:
    {organization.get('name')} ({organization.get('id')})
    Adress: {organization.get('adress')},
    Contacts:''')
    for contact in organization.get('contacts'):
        print(f"        {contact.get('name')} ({contact.get('position')}) ID: {contact.get('id')}")
    print('_'*50)

def get_organization(name):
    for organization in organizations:
        if organization.get('name') == name:
            return organization


def add_contact():
    organization = get_organization(selected_organization)
    name = input('Name: ')
    position = input('Position: ')
    id = int(input('ID: '))
    organization.get('contacts').append({
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
        'contacts': {}
    }
    organizations.append(org)

def select_organization():
    for i in range(len(organizations)):
        print(f"{i} - {organizations[i].get('name')}")
    while True:
        global selected_organization
        selected_organization_num = int(input("Enter number of organization: "))
        try:
            selected_organization = organizations[selected_organization_num].get('name')
        except:
            print("Invalid number")
        else:
            break

def stop_running():
    sys.exit()

def reset_select():
    global selected_organization
    selected_organization = None


def main():
    selected_organization = None
    while True:
        if selected_organization:
            print(f'Selected: {selected_organization}')
            response = input('Add contact - 1\n'
                             'Organization info - 2\n'
                             'Back - B\n')
            activities = {'1': add_contact,
                          '2': print_info,
                          'B': reset_select}

        else:
            response = input('Add organization - 1\n'
                             'Select organizatoin - 2\n'
                             'Exit - E\n')
            activities = {'1':add_organization,
                          '2':select_organization,
                          'E':stop_running}

        activities.get(response, lambda : print('Invalid response'))()
        print()

if __name__ == '__main__':
    main()