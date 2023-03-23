#!/usr/bin/python3
"""
A script that takes in args and
displays all values in the states but
safe from MySQLi
"""

if __name__ == '__main__':
    import MySQLdb as db
    from sys import argv
    """
    Access the database and get the states from
    the database
    """
    conn = db.connect(host='localhost', port=3306, user=argv[1],
                      passwd=argv[2], db=argv[3])
    query = "SELECT * FROM states WHERE name = %s"
    params = (argv[4],)
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    for row in rows:
        print(row)
