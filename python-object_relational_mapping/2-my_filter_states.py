#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where the name matches the user input.

Connects to a MySQL server on localhost at port 3306, retrieves
matching rows from the states table ordered by id, and prints them.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    # Execute SQL query using format()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Print results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
