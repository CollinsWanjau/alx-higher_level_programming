#!/usr/bin/python3
"""
Takes in an arg and displays all 
values in the the state table where n
ame matches args
"""

if __name__ == '__main__':
    import MySQLdb as db
    from sys import argv
    """
    Access the database and get the states
    from the database
    """
    conn  = db.connect(host="localhost", port=3306, user=argv[1],
                      passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
