#!/usr/bin/python3
"""script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""

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
            "SELECT * from states WHERE name LIKE BINARY\
                    '{}' ORDER BY id".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
