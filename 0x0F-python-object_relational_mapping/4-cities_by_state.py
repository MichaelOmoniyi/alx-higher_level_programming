#!/usr/bin/python3
import MySQLdb
import sys

username = str(sys.argv[1])
password = str(sys.argv[2])
dbName = str(sys.argv[3])
db = MySQLdb.connect("localhost", username, password, dbName)
dbCur = db.cursor()
dbCur.execute("""SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON states.id = cities.state_id
        ORDER BY id ASC""")
rows = dbCur.fetchall()
for row in rows:
    print(row)
db.close()
