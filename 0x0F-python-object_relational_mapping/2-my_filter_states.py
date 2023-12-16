#!/usr/bin/python3
""" Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY states.id ASC".format(state_name))

    rows = cursor.fetchall()

    for state in rows:
        print(state)

    cursor.close()
    db.close()
