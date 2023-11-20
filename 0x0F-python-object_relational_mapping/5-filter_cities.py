#!/usr/bin/python3
"""
This script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

username = str(sys.argv[1])
password = str(sys.argv[2])
dbName = str(sys.argv[3])
state = str(sys.argv[4])
db = MySQLdb.connect("localhost", username, password, dbName)
dbCur = db.cursor()
dbCur.execute("""SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON states.id = cities.state_id
        ORDER BY id ASC""")
rows = dbCur.fetchall()
statesArr = []
for row in rows:
    if row[2] == state:
        statesArr.append(row[1])
for s in range(0, len(statesArr)):
    if s < (len(statesArr) - 1):
        print("{}, ".format(statesArr[s]), end="")
    else:
        print(statesArr[s])
cur.close()
db.close()
