import sqlite3
import names


from random import randrange, randint
from datetime import timedelta, date


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_birthdate(year1, year2):
    return random_date(date(year1, 1, 1), date(year2, 1, 1))


def random_start_date(year1, year2):
    return date(randint(year1, year2), 9, 1)


connection = sqlite3.connect(r"C:\Users\masha\PycharmProjects\pythonProject\123\lyceum_db.db")
cursor = connection.cursor()

students = list(map(lambda i: (names.get_first_name(),
                               names.get_last_name(),
                               random_start_date(2019, 2021),
                               random_birthdate(2004, 2007)), range(1000)))
for student in students:
    query = "INSERT INTO student(first_name, last_name, start_study, birthday) VALUES (?, ?, ?, ?)"
    cursor.execute(query, student)
connection.commit()


teachers = list(map(lambda i: (names.get_first_name(),
                               names.get_last_name(),
                               random_start_date(2000, 2021),
                               random_birthdate(1950, 1980)), range(50)))

for teacher in teachers:
    query = "INSERT INTO teacher(first_name, last_name, start_work, birthday) VALUES (?, ?, ?, ?)"
    cursor.execute(query, teacher)
connection.commit()

