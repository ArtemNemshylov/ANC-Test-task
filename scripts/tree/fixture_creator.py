import csv
from faker import Faker
from random import choice

fake = Faker()
positions = ['Analyst', 'Developer', 'Designer', 'Project Manager', 'Accountant', 'HR', 'Sales', 'Support',
             'Consultant']

with open('../../data/tree/employees.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['full_ame', 'position', 'date_of_employment', 'email', 'level'])

    for level in range(1, 11):
        for number_of_employees in range(3 ** level):
            name = fake.name()
            position = choice(positions)
            date_of_birth = fake.date()
            email = fake.safe_email()

            writer.writerow([name, position, date_of_birth, email, level])
