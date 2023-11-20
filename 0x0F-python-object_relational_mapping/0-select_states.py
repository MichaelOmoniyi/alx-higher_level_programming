#!/usr/bin/python3
"""
This script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

username = str(sys.argv[1])
password = str(sys.argv[2])
dbName = str(sys.argv[3])
tableName = "states"
db = MySQLdb.connect(host='localhost', user=username,
                     passwd=password, db=dbName)
dbCur = db.cursor()
dbCur.execute("""SELECT id, name FROM {} ORDER BY id ASC""".format(tableName))
results = dbCur.fetchall()

for row in results:
    print(row)
cur.close()
