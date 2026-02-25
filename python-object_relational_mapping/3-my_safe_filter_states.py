#!/usr/bin/python3
"""
Script that lists all states with a name matching the argument
from the database hbtn_0e_0_usa (safe from SQL injection).
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL database and query states safely."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
