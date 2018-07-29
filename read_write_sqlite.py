import csv
import sqlite3

conn = sqlite3.connect('bdgeoteste.db')
cursor = conn.cursor()

with open('minerais1.csv') as csvfile:
    rows = csv.reader(csvfile, delimiter = ',')

    for row in rows:
        cursor.execute('INSERT INTO litotypes_nomenclature (name, code) VALUES (?, ?)', [row[0], row[1]])
        cursor.execute('INSERT INTO litotypes_nomenclature (name, code) VALUES (?, ?)', [row[2], row[3]])
        cursor.execute('INSERT INTO litotypes_nomenclature (name, code) VALUES (?, ?)', [row[4], row[5]])
        cursor.execute('INSERT INTO litotypes_nomenclature (name, code) VALUES (?, ?)', [row[6], row[7]])
conn.commit()
conn.close()

print('Data saved!')