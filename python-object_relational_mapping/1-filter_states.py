#!/usr/bin/python3
"""
Lists all states from the database where the name starts with uppercase 'N'.

Connects to a MySQL server on localhost at port 3306, retrieves matching rows
from the states table ordered by id in ascending order, and prints them.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
