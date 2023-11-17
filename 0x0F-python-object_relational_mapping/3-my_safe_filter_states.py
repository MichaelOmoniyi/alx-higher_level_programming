#!/usr/bin/python3
import MySQLdb
import sys

username = str(sys.argv[1])
password = str(sys.argv[2])
dbName = str(sys.argv[3])
name = str(sys.argv[4])
tbName = "states"
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=username,
                         password=password, database=dbName)
    dbCur = db.cursor()
    dbCur.execute("""SELECT id, name FROM {} ORDER BY id""".format(tbName))
    rows = dbCur.fetchall()

    for row in rows:
        if row[1] == name:
            print(row)
cur.close()
db.close()
