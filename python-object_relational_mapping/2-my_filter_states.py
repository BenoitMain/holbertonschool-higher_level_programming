#!/usr/bin/python3
"""Script that lists all states where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    # Utilisation de format comme demandé (attention à l’injection SQL)
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
