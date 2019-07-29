import sqlite3

name="Ni"
conn = sqlite3.connect("movies.db")
c = conn.cursor()
films = c.execute('SELECT * FROM movies WHERE name LIKE ?', ('%' + name + '%',))
for i in films:
    print(i[1])