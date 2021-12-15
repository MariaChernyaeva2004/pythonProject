import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
result = cursor.execute("""SELECT title FROM films
            WHERE duration <= 85""").fetchall()

for elem in result:
    print(elem[0])
