#!/usr/bin/env python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

This module connects to a MySQL database and retrieves all records from the
'states' table, ordered by id in ascending order. The script takes three
command-line arguments: MySQL username, password, and database name.

Usage:
    python3 0-select_states.py <mysql_user> <mysql_password> <database_name>
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
