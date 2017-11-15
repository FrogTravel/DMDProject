import sqlite3
#http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

print(sqlite3.sqlite_version)

conn = sqlite3.connect(r"/Users/ekaterina/PycharmProjects/DMDProject3/myfirstdb.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS TestTable ("
               "id integer PRIMARY KEY AUTOINCREMENT,"
               "first_name text NOT NULL,"
               "last_name text NOT NULL);")
cursor.execute("INSERT INTO TestTable (first_name, last_name) VALUES (\"Mary\", \"Johns\"), (\"Bred\", \"Stevens\");")
cursor.execute("SELECT * FROM TestTable;")
rows = cursor.fetchall()
for row in rows:
    print(row)