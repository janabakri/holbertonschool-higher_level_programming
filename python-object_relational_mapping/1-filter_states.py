#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where the name starts with uppercase 'N'.

Connects to a MySQL server on localhost at port 3306,
retrieves matching rows from the states table ordered by id,
and prints them.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
