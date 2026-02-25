#!/usr/bin/python3
"""
Displays all states from the database hbtn_0e_0_usa
where the name matches the argument given by the user.

Connects to a MySQL server on localhost at port 3306,
retrieves matching rows from the states table ordered by id,
and prints them.

This version is safe from SQL injection.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    # Safe query using parameterized placeholder
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
