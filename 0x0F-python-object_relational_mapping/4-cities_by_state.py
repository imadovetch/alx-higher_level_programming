#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")

    citys = cursor.fetchall()

    for city in citys:
        print(city)

    cursor.close()
    db.close()
