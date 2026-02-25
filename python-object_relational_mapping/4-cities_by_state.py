#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""
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
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    for city_id, city_name, state_name in rows:
        print("({}, '{}', '{}')".format(city_id, city_name, state_name))

    cursor.close()
    db.close()
    
