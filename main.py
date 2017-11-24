import sqlite3
import createQueries, selectQueries
#http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/


conn = sqlite3.connect(r"C:\Users\Aline\PycharmProjects\DMDProject\myfirstdb.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS TestTable ("
#                "id integer PRIMARY KEY AUTOINCREMENT,"
#                "first_name text NOT NULL,"
#                "last_name text NOT NULL);")
# cursor.execute("INSERT INTO TestTable (first_name, last_name) VALUES (\"Mary\", \"Johns\"), (\"Bred\", \"Stevens\");")
cursor.execute(createQueries.CREATE_STATE)
cursor.execute(createQueries.CREATE_LOCATION)
cursor.execute(createQueries.CREATE_CLIENT)
cursor.execute(createQueries.CREATE_LIVES_AT_RELATION_TABLE)
cursor.execute(createQueries.CREATE_MANAGER)
cursor.execute(createQueries.CREATE_ALL_CARS)
cursor.execute(createQueries.CREATE_CAR_LOG)
cursor.execute(createQueries.CREATE_REFILL_STATION)
cursor.execute(createQueries.CREATE_CHARGE_EVENT)
cursor.execute(createQueries.CREATE_ORDER)
cursor.execute(createQueries.CREATE_PAYMENT)
cursor.execute(createQueries.CREATE_VIDEO)

# query1: red car
print("Possible cars:")
cursor.execute(selectQueries.RED_CAR)
row = cursor.fetchone()
while row is not None:
    print("Model: {0}, number {1}\n".format(row[0], row[1]))
    row = cursor.fetchone()

# query2: charger statistics
# text = input("Write the date to get the statictics: ")

cursor.execute(selectQueries.ALL_CARS)
row = cursor.fetchone()
count = row[0]

# TODO cursor.execute("SELECT " + DBStructure.ALL_CARS_FIELD_NUMBER + ", color" + " FROM All_Cars WHERE color = '%s'" %'red')

# rows = cursor.fetchall()
# for row in rows:
#     print(row)
