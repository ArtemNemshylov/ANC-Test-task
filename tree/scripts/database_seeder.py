from faker import Faker
from random import choice
from tree.models import Employee

fake = Faker()
positions = ['Analyst', 'Developer', 'Designer', 'Project Manager', 'Accountant', 'HR', 'Sales', 'Support',
             'Consultant']


def first_seed():
    for level in range(1, 11):
        for number_of_employees in range(3 ** level):
            name = fake.name()
            position = choice(positions)
            date_of_birth = fake.date()
            email = fake.safe_email()
            while Employee.objects.filter(email=email).exists():
                email = fake.safe_email()
            Employee.objects.create(full_name=name, position=position, date_of_employment=date_of_birth, email=email,
                                    level=level)

