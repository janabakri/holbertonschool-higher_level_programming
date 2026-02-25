#!/usr/bin/python3
"""Lists all states with a space at the end of each line"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    for row in cursor.fetchall():
        # Add a space at the end of the line
        print("({}, '{}') ".format(row[0], row[1]))  # Notice the space before the closing parenthesis
        
    cursor.close()
    db.close()
