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


def print_info(organization):
    print(f'''
Organization:
{organization.get('name')} ({organization.get('id')})
Adress: {organization.get('adress')},
Contacts:''')
    for contact in organization.get('contacts'):
        print(f"    {contact.get('name')} ({contact.get('position')}) ID: {contact.get('id')}")
    print('_'*50)

def get_organization(name):
    for organization in organizations:
        if organization.get('name') == name:
            return organization


def add_contact(organisation, name: str, position: str, id: int):
    organisation.get('contacts').append({
        'name': name,
        'position': position,
        'id': id
    })



while True:
    response = input('Add contact? (Y/N)')
    if response == 'Y':
        organization_name = input('Organization: ')
        organization = get_organization(organization_name)
        name = input('Name: ')
        position = input('Position: ')
        id = int(input('ID: '))
        add_contact(organization, name, position, id)
        print_info(organization)
    else:
        break