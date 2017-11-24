import sqlite3
import createQueries
#http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/


conn = sqlite3.connect(r"/Users/ekaterina/PycharmProjects/DMDProject3/myfirstdb.db")
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS TestTable ("
#                "id integer PRIMARY KEY AUTOINCREMENT,"
#                "first_name text NOT NULL,"
#                "last_name text NOT NULL);")
# cursor.execute("INSERT INTO TestTable (first_name, last_name) VALUES (\"Mary\", \"Johns\"), (\"Bred\", \"Stevens\");")

cursor.execute(createQueries.CREATE_LOCATION)
cursor.execute(createQueries.CREATE_CLIENT)
cursor.execute(createQueries.CREATE_LIVES_AT_RELATION_TABLE)
cursor.execute(createQueries.CREATE_MANAGER)
cursor.execute(createQueries.CREATE_ALL_CARS)
cursor.execute(createQueries.CREATE_CAR_LOG)
cursor.execute(createQueries.CREATE_REFILL_STATION)
cursor.execute(createQueries.CREATE_REFILL_STATION_HISTORY)
cursor.execute(createQueries.CREATE_ORDER)
cursor.execute(createQueries.CREATE_PAYMENT)
cursor.execute(createQueries.CREATE_VIDEO)



# rows = cursor.fetchall()
# for row in rows:
#     print(row)
