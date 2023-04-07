import sqlite3
from flask import Flask, render_template, request

connection = sqlite3.connect('my_db.db')
cur = connection.cursor()
cur.execute('DROP TABLE IF EXISTS list_service;')

cur.execute('''CREATE TABLE IF NOT EXISTS list_service ( 
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Record TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    Car TEXT NOT NULL,
                    PartChange TEXT NOT NULL);''')
cur.close()

def insert_records(records):
    try:
        sqlite_connection = sqlite3.connect('my_db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к БД")

        sqlite_insert = 'INSERT INTO list_service (Car, PartChange) VALUES (?, ?);'

        cursor.executemany(sqlite_insert, records)
        sqlite_connection.commit()
        print("Записи вставлены", cursor.rowcount)
        sqlite_connection.commit()
        #cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение закрыто")

records_to_insert = [('Car1', 'PartItemName1'),
            ('Car2', 'PartItemName2'),
            ('Car3', 'PartItemName3'),
            ('Car4', 'PartItemName4'),
            ('Car5', 'PartItemName5'),
            ('Car6', 'PartItemName6'),
            ('Car7', 'PartItemName7'),
            ('Car8', 'PartItemName8'),
            ('Car9', 'PartItemName9'),
            ('Car10', 'PartItemName10'),
            ('Car11', 'PartItemName11'),
            ('Car12', 'PartItemName12'),
            ('Car13', 'PartItemName13'),
            ('Car14', 'PartItemName14'),
            ('Car15', 'PartItemName15'),
            ('Car16', 'PartItemName16'),
            ('Car17', 'PartItemName17'),
            ('Car18', 'PartItemName18'),
            ('Car19', 'PartItemName19'),
            ('Car20', 'PartItemName20'),
            ('Car21', 'PartItemName21')]

insert_records(records_to_insert)

connection = sqlite3.connect('my_db.db')
cur = connection.cursor()
list_service = cur.execute('SELECT * FROM list_service').fetchall()
print(list_service)

app = Flask(__name__)

@app.route('/')
def index():
    db = sqlite3.connect('my_db.db')
    conn = db.cursor()
    records = conn.execute("SELECT * FROM list_service").fetchall()
    conn.close()
    return render_template("index.html", change_list=records)

app.run(port=5000, host='127.0.0.1')