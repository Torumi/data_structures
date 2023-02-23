from os import system
system('pip install -r requirements.txt')
system('cls')



import sys
import json

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

'''Loads organizations from file'''
with (open('organizations.json', 'r')) as openfile:
    organizations = json.load(openfile)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def select_organization():
    """Selects organizations"""
    if len(organizations) != 0:

        table = Table(
            show_header=False,
            show_lines=False,
            show_edge=False
        )
        chunked_list = list(chunks(organizations, 4))
        for _ in range(4):
            table.add_column()

        index = 0
        for row in chunked_list:
            table.add_row(f'{row[0].get("name")} - {index}', f'{row[1].get("name")} - {index + 1}', f'{row[2].get("name")} - {index + 2}', f'{row[3].get("name")} - {index + 3}')
            index += 4

        console.print(table)

        while True:
            try:
                selected_organization_num = int(console.input("[b]Enter number of organization[/]: "))
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

    output = f'''
[u b]{selected_organization.get('name')} ({selected_organization.get('id')})[/]
    [b]Adress[/]: {selected_organization.get('adress')}
    [b]Income[/]: {selected_organization.get('income')} $
    [b]Contacts[/]:
'''

    for contact in selected_organization.get('contacts'):
        output += f"        {contact.get('name')} ({contact.get('position')}) ID: {contact.get('id')}\n"
    print('_' * 50)

    panel = Panel(output)
    panel.title = "[b]Organization[/]"
    console.print(panel)




def add_contact():
    """Adds a contact to selected organization"""
    name = input('Name: ')
    position = input('Position: ')
    while True:
        try:
            contact_id = int(input('ID: '))
        except ValueError:
            console.print('ID is a number', style='bold red')
        else:
            break

    selected_organization.get('contacts').append({
        'name': name,
        'position': position,
        'id': contact_id
    })
    console.print(f'Added [b]{name}[/] to [b]{selected_organization.get("name")}[/]', style='yellow')


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
                confirm = console.input('\n[yellow]Are you sure?[b][Y/N upper case][/]')
                if confirm == 'Y':
                    deleted_contact = selected_organization.get('contacts').pop(contact_to_del_num)
                    console.print(
                            f"[b]{deleted_contact.get('name')} ({deleted_contact.get('position')}) ID: {deleted_contact.get('id')}[/] HAS BEEN DELETED", style='yellow')
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
    console.print(f'Added [b]{name}[/]', style='yellow')


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
                confirm = console.input('\n[yellow]Are you sure?[b][Y/N upper case][/]')
                if confirm == 'Y':
                    deleted_organization = organizations.pop(organization_to_del_num)
                    console.print(f"[b]{deleted_organization.get('name')}[/] HAS BEEN DELETED", style='yellow')
                break
    else:
        print('There are no organizations yet')


def edit_income():
    income = int(input("Income: "))
    selected_organization["income"] = income


def print_income_top():
    table = Table(
        title='TOP 5 organizations by income',
        show_edge=False,
        title_style='bold',
        header_style='bold',
        leading=1
    )
    table.add_column('Place')
    table.add_column('Organization')
    table.add_column('Income', style='bold green')

    sorted_orgs = list(reversed(sorted(organizations, key=lambda d: d['income'])))
    for index, company in enumerate(sorted_orgs[:5]):
        table.add_row(str(index + 1), company.get('name'), f'{company.get("income")}$')

    console.print(table)


def get_organization_by_id():
    id_list = [org.get('id') for org in organizations]
    while True:
        org_id = input("ID: ")
        try:
            index = id_list.index(org_id)
        except ValueError:
            console.print('No such ID', style='bold red')
        else:
            global selected_organization
            selected_organization = organizations[index]
            break


def main():
    while True:
        if selected_organization:
            console.print(f'Selected: [bold]{selected_organization.get("name")}[/]')

            table = Table(
                show_header=False,
                show_lines=False,
                show_edge=False
            )
            table.add_column()
            table.add_column(style='bold green')
            table.add_row('Add contact', 'A')
            table.add_row('Delete contact', 'D')
            table.add_row('Organization info', 'I')
            table.add_row('Edit income', 'E')
            table.add_row('Back', 'B')

            response = console.input(table).lower()
            activities = {'a': add_contact,
                          'd': delete_contact,
                          'i': print_info,
                          'e': edit_income,
                          'b': reset_selection}

        else:
            table = Table(
                show_header=False,
                show_lines=False,
                show_edge=False
            )
            table.add_column()
            table.add_column(style='bold green')
            table.add_row('Add organization', 'A')
            table.add_row('Delete organization', 'D')
            table.add_row('Select organization ', 'S')
            table.add_row('Get TOP 5 income companies', 'T')
            table.add_row('Find organization by ID', 'F')
            table.add_row('Exit', 'E')

            response = console.input(table).lower()
            activities = {'a': add_organization,
                          'd': delete_organization,
                          's': select_organization,
                          't': print_income_top,
                          'f': get_organization_by_id,
                          'e': lambda: sys.exit()}

        activities.get(response, lambda: console.print('Invalid response', style = 'bold red'))()

        with (open('organizations.json', 'w')) as outfile:
            json.dump(organizations, outfile, indent=4)
        print('\n' + '*' * 30 + '\n')


if __name__ == '__main__':
    selected_organization = None
    main()
