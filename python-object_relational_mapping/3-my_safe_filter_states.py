#!/usr/bin/python3
"""
Script that lists all states with a given name from the database hbtn_0e_0_usa
Safe from SQL injection
"""

import MySQLdb
import sys


def safe_filter_states():
    """
    Function to filter states safely without SQL injection vulnerability
    """
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> "
              "<database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query with parameterized query (safe from SQL injection)
    # The %s placeholder is used for parameterized queries in MySQLdb
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    try:
        cursor.execute(query, (state_name,))
        
        # Fetch all the rows
        results = cursor.fetchall()
        
        # Display the results
        for row in results:
            print(row)
            
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        sys.exit(1)
    
    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    safe_filter_states()
