import sqlite3

connection = sqlite3.connect("music_db.sqlite")
cursor = connection.cursor()
genre = input("Введите название жанра(с заглавной буквы):")

result = cursor.execute(f"""SELECT DISTINCT a.name FROM genre gen, track tr, album alb, artist a WHERE tr.genreid = gen.genreid
AND tr.albumid = alb.albumid
AND alb.artistid = a.artistid
AND gen.name = '{genre}'
ORDER BY a.name;""")
for elem in result:
    print(elem[0])