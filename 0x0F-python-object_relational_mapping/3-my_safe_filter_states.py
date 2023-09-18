#!/usr/bin/python3
"""script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from MySQL injections!"""

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
            "SELECT * from states WHERE name LIKE BINARY %s ORDER BY id",
            (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
