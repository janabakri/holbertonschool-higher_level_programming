#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

This script connects to a MySQL database running on localhost at port 3306,
retrieves all records from the states table where the name starts with 'N',
and displays them sorted in ascending order by states.id.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>

Example:
    ./1-filter_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute query to get all states with name starting with 'N'
    # Using BINARY to ensure case sensitivity (upper N only)
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Display each row as a tuple
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

