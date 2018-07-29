import sqlite3

conn = sqlite3.connect('bdgeoteste.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE litotypes_nomenclature (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT NOT NULL
);
''')

print ('Table "litotypes_nomenclature" created!')

conn.close()
