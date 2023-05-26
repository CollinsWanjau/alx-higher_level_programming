#!/usr/bin/python3
"""
Lists all cities in ASC order
"""

if __name__ == '__main__':
    import MySQLdb as db
    from sys import argv
    conn = db.connect(host="localhost", port=3306, user=argv[1],
                      passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON\
            state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
