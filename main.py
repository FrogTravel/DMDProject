import sqlite3

import createQueries
import selectQueries
import insertData
import DBStructure


conn = sqlite3.connect(DBStructure.DB_FILENAME)
cursor = conn.cursor()

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

insertData.gen_random_data(cursor)

selectQueries.start(cursor)

conn.commit()
conn.close()