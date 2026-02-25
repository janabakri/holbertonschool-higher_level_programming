#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

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
    
    # Create a cursor object to execute queries
    cursor = db.cursor()
    
    # Execute query to get all states sorted by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
