#!/usr/bin/python3
"""
Script that safely lists all states from the database hbtn_0e_0_usa
where name matches the provided argument.
Prevents SQL injection by using parameterized queries.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to MySQL database and retrieves matching states safely.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cur = db.cursor()

    # Execute safe query using parameterized input
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connections
    cur.close()
    db.close()
