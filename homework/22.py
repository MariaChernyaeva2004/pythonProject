import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
result = cursor.execute("""SELECT DISTINCT title FROM genres WHERE id 
IN (SELECT genre FROM films WHERE year == 2010 or year == 2011)""")
for elem in result:
    print(elem[0])