from faker import Faker
from random import choice
from django.db import transaction
from tree.models import Employee

fake = Faker()
positions = ['Analyst', 'Developer', 'Designer', 'Project Manager', 'Accountant', 'HR', 'Sales', 'Support',
             'Consultant']


def first_seed():
    email_set = set()
    all_employees = []
    levels_employees = {}

    for level in range(1, 11):
        current_level_employees = []
        num_employees = 3 ** level

        for _ in range(num_employees):
            while True:
                email = fake.safe_email()
                if email not in email_set:
                    email_set.add(email)
                    break

            name = fake.name()
            position = choice(positions)
            date_of_birth = fake.date()

            employee = Employee(
                full_name=name,
                position=position,
                date_of_employment=date_of_birth,
                email=email,
                level=level
            )
            current_level_employees.append(employee)

        all_employees.extend(current_level_employees)
        levels_employees[level] = current_level_employees


    # Сохранение всех объектов без chief
    Employee.objects.bulk_create(all_employees)

    # Сохранение связей с chief
    for level in range(2, 11):
        chiefs = levels_employees.get(level - 1, [])
        subordinates = levels_employees.get(level, [])
        if chiefs:
            for index, subordinate in enumerate(subordinates):
                chief_index = (index // 3) % len(chiefs)
                subordinate.chief = chiefs[chief_index]
                subordinate.save()
