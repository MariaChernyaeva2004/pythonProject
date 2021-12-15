import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
template = input("введите шаблон: ")
result = cursor.execute(f"""
SELECT title FROM films
WHERE title LIKE ?
""").fetchall()

print(result)