#!/usr/bin/python3


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
    cur.execute(
        "SELECT cities_id, city_name, state_name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY name = %s ORDER BY id ASC",
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
