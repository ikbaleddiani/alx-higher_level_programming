#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

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
    cursor.execute(
            "SELECT * from states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
