#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
with their corresponding state name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user, password, db_name = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
