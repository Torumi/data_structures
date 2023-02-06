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
Contacts: {len(organization.get('contacts'))}
{'_' * 20}
            ''')


def add_contact(organisation, name: str, position: str, id: int):
    organisation.get('contacts').append({
        'name': name,
        'position': position,
        'id': id
    })



while True:
    print_info(organizations[0])
    response = input('Add contact? (Y/N)')
    if response == 'Y':
        name = input('Name: ')
        position = input('Position: ')
        id = int(input('ID: '))
        add_contact(organizations[0], name, position, id)
    else:
        break
