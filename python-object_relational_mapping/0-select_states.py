#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Display results
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
