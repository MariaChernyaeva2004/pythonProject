import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()

result = cursor.execute("""
SELECT title FROM films
WHERE title LIKE '%?'
""").fetchmany(10)

print(result)

