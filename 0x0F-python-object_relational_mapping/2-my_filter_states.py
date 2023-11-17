#!/usr/bin/python3
import MySQLdb
import sys

username = str(sys.argv[1])
password = str(sys.argv[2])
dbName = str(sys.argv[3])
name = str(sys.argv[4])
tableName = "states"
db = MySQLdb.connect(host='localhost', user=username,
                     passwd=password, db=dbName)
dbCur = db.cursor()
dbCur.execute("""SELECT id, name FROM {} ORDER BY id ASC""".format(tableName))
results = dbCur.fetchall()

for row in results:
    if row[1] == name:
        print(row)
cur.close()
db.close()
