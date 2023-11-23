#!/usr/bin/python3
"""
This script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    dbName = str(sys.argv[3])
    tableName = "states"
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName)
    dbCur = db.cursor()
    dbCur.execute("""SELECT id, name FROM {} ORDER BY id ASC""".
                  format(tableName))
    results = dbCur.fetchall()

    for row in results:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
