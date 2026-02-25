#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
with their corresponding state name.

Connects to a MySQL server on localhost at port 3306,
retrieves all cities ordered by cities.id using a single query,
and prints them as (id, city_name, state_name).
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    # Single execute with JOIN to get city id, city name, and state name
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)

    # Print each row
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
