import sqlite3

import DBStructure

conn = sqlite3.connect(DBStructure.DB_FILENAME)
cursor = conn.cursor()
