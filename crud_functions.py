import sqlite3

conect = sqlite3.connect('database.db')

def initiate_db():
    cursor = conect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL,
        description TEXT, 
        price INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
    ''')

    # for i in range(1, 5):
    #      cursor.execute(' INSERT INTO Products(title, description, price) VALUES (?, ?, ?)', (f'Продукт{i}', f'Описание{i}', i*100))
    # for i in range(1, 2):
    #     cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)', ('Сергей', 'wer@mail.ru', 18, 1000))

    conect.commit()
    conect.close()

def clear():
    cursor = conect.cursor()
    for i in range(1, 5):
        cursor.execute(' DELETE FROM Products WHERE title = ?', (f'Продукт{i}',))
    conect.commit()
    conect.close()

def get_all_products():
    cursor = conect.cursor()
    cursor.execute(' SELECT * FROM Products')
    conect.commit()
    return cursor.fetchall()

def add_user(username, email, age):
    cursor = conect.cursor()
    cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)', (username, email, age, 1000))
    conect.commit()

def is_incluted(username):
    cursor = conect.cursor()
    rez = cursor.execute(f' SELECT * FROM Users WHERE username = ?', (username, )).fetchall()
    if rez != []:
        conect.commit()
        return True
    else:
        conect.commit()
        return False
