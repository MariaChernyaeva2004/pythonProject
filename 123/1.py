import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
id_field = input("Введите id: ")
title = input("Введите название: ")
year = input("Введите год: ")
genre_id = input("Введите id жанра: ")
duration = input("Введите продолжительность: ")
query = f"""INSERT INTO films(id, title, year, genre, duration) 
VALUES (?, ?, ?, ?, ?)"""
print(query)
result = cursor.execute(query, [id_field, title, year, genre_id, duration])
connection.commit()