#!/usr/bin/python3
"""
Lists all states from the specified MySQL database.

This script connects to a MySQL server running on localhost at port 3306,
retrieves all rows from the states table ordered by id in ascending order,
and prints them to standard output.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and prints all states ordered by id.
    """
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
