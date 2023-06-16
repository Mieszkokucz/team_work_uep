import csv
import random
import os

def generate_salary():
    return random.randint(1000, 10000)

def generate_employees_csv():
    header = ['Imię', 'Nazwisko', 'Pensja']
    employees = [
        ['Jan', 'Kowalski', generate_salary()],
        ['Anna', 'Nowak', generate_salary()],
        ['Piotr', 'Wiśniewski', generate_salary()],
        ['Maria', 'Jankowska', generate_salary()],
        ['Krzysztof', 'Kaczmarek', generate_salary()]
        # Dodaj więcej pracowników według potrzeb
    ]


    if not os.path.exists('data'):
        os.makedirs('data')


    with open('data/pracownicy.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(employees)

generate_employees_csv()

