# Companies's employees and tasks assign to them.

company = {
    'alice': ['loan managing','weekly closing'],
    'brayn' : ['marketing head'],
    'charlie': ['finance head','monthly closing','salary distributor'],
    'david': ['operations head','staff management']
}

def company_structure():
    print('Company Structure:')
    for employee, roles in company.items():
        print(f'{employee}: {roles}')


def add_employee(name, *roles):
    if name in company:
        print(f'Employee {name} already exists in the company.')
    else:
        company[name] = roles
        print(f'Employee {name} added successfully with roles: {roles}')

def remove_employee(name):
    if name in company:
        del company[name]
        print(f'Employee {name} removed successfully from the company.')
    else:
        print(f'Employee {name} not found in the company.')


def update_roles(name, *new_roles):
    if name in company:
        company[name] = new_roles
        print(f'new roles assign to {name} are {new_roles}')
    else:
        print(f'Employee {name} not found in the company.')

def add_roles(name, *new_roles):
    if name in company:
        company[name].extend(new_roles)
        print(f'Further roles assigned to {name} are {new_roles}')
    else:
        print(f'Employee {name} not found in the company.')
