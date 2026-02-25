#!/usr/bin/python3
"""
Takes an argument and displays all values in the states table where name matches the argument

This script connects to a MySQL database running on localhost at port 3306,
takes a state name as an argument, and displays all matching states
sorted in ascending order by states.id.

Usage:
    ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute query to get states with name matching the argument
    # Using format to create the SQL query with user input (as required)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Display each row as a tuple
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
