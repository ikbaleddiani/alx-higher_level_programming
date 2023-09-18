#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    kwargs = {
            "host": 'localhost',
            "port": 3306,
            "user": argv[1],
            "passwd": argv[2],
            "db": argv[3]}
    connection = MySQLdb.connect(**kwargs)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name ,states.name\
            from cities JOIN states WHERE cities.state_id = states.id\
            ORDER BY cities.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
