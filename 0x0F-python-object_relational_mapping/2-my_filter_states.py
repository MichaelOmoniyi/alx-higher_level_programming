#!/usr/bin/python3
"""
This script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    dbName = str(sys.argv[3])
    name = str(sys.argv[4])
    tableName = "states"
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName)
    dbCur = db.cursor()
    dbCur.execute("""SELECT id, name FROM {} ORDER BY id ASC""".
                  format(tableName))
    results = dbCur.fetchall()

    for row in results:
        if row[1] == name:
            print(row)
    cur.close()
    db.close()
