organizations = [
    {
        'name':'Tesla Motors',
        'adress':'Tesla ave 1, USA',
        'id':'8646678',
        'contacts':[
            {
                'name':'Elon',
                'position':'CEO',
                'id':1
            },
            {
                'name':'Jenifer',
                'position':'CTO',
                'id':2
            }
        ]
    },
    {
            'name':'Apple',
            'adress':'Apple Inc., 1 Infinite Loop, Cupertino, CA 95014, USA.',
            'id':'942404110',
            'contacts':[
                {
                    'name':'Tim',
                    'position':'CEO',
                    'id':1
                },
                {
                    'name':'Steve',
                    'position':'CTO',
                    'id':2
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
{'_'*20}
            ''')

print_info(organizations[0])