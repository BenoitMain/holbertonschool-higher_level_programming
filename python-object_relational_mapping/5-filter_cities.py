#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <mysql username>
<mysql password> <database name> <state name>

Arguments:
    mysql username: MySQL username to connect with
    mysql password: MySQL password to connect with
    database name: Database to use
    state name: State to filter cities by
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    state = sys.argv[4]
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (state,))
    villes = [row[0] for row in cur.fetchall()]
    if villes:
        print(", ".join(villes))
    cur.close()
    db.close()
