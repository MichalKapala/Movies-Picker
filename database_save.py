import sqlite3

class Database:
    def __init__(self, name):
        self.name = name


    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.name)
        except Exception as error:
            print(error)


    def create_table(self):
        if self.conn != None:
            try:
                c = self.conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS movies(id integer , name text RIMARY KEY NOT NULL UNIQUE, score float, genre text)')
                self.conn.commit()
            except Exception as error:
                print(error)
        else:
            print("Blad, nie polaczona z baza danych")


    def insert(self, id, nazwa, ocena, gatunek):
        if self.conn != None:
            try:
                c = self.conn.cursor()
                c.execute('INSERT INTO movies VALUES(?,?,?,?)', (id, nazwa[3:], ocena, gatunek))
                self.conn.commit()
            except Exception as error:
                print(error)
        else:
            print("Blad, nie polaczona z baza danych")






