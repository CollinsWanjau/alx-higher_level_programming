#!/usr/bin/python3
"""
Lists all cities in ASC order
"""

if __name__ == '__main__':
    import MySQLdb as db
    from sys import argv
    conn = db.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    query = ""
