import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()

id_field = input("введите айди:")

cursor.execute()