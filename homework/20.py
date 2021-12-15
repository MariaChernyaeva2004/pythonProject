import sqlite3
connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
result = cursor.execute("""SELECT DISTINCT films.title FROM films
 WHERE title LIKE "%Астерикс%" AND title NOT LIKE "%Обеликс%" """)
for elem in result:
    print(elem[0])
