#!/usr/bin/python3
"""
Filter states starting with 'N' from MySQL database.

This script connects to a MySQL database and retrieves all states whose names
start with the letter 'N' (case-sensitive), ordered by ID in ascending order.

"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        port=3306,
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
