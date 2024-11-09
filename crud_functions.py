import sqlite3

conect = sqlite3.connect('database.db')
cursor = conect.cursor()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products( 
        id INTEGER PRIMARY KEY, 
        title TEXT NOT NULL,
        description TEXT, 
        price INTEGER NOT NULL
        )
    ''')
    # for i in range(1, 5):
    #     cursor.execute(' INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)', (i, f'Продукт{i}', f'Описание{i}', i*100))

def clear():
    for i in range(1, 5):
        cursor.execute(' DELETE FROM Products WHERE title = ?', (f'Продукт{i}',))

def get_all_products():
    cursor.execute(' SELECT * FROM Products')
    return cursor.fetchall()
