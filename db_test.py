# Мой файл для тестирования sqlite3-базы

import sqlite3

db = sqlite3.connect('app.db')
cur = db.cursor()
cur.execute('SELECT * FROM lecturer')
fall = cur.fetchall()
print(fall)