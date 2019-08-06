import sqlite3
import os
import time

def login_request(login, password):
    try:
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        d = c.execute('SELECT * FROM logins WHERE login=(?) AND haslo=(?)',(login, password))
        if  d.fetchone() == None:
            return "Bledne haslo lub login"
        return True
    except Exception as error:
        return error


def register():
    email = input("Wprowadz email: ")
    login = input("Wprowadz login: ")
    psswd = input("Wprowadz haslo: ")
    psswdr = input("Wprowadz haslo ponownie: ")
    if(psswd != psswdr):
        print("Wprowadzone hasla sie roznia")
        time.sleep(2)
        os.system('cls')
    try:
        conn  = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute('INSERT INTO logins VALUES(?,?,?)', (login, psswd, email))
        conn.commit()
        return
    except Exception as error:
        print(error)


register()
#login_request()