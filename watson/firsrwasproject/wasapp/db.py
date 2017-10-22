# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import dbm
import sqlite3
# Open database, creating it if necessary.


def testfunction(dataarray):

    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print (row)
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

    # Open database, creating it if necessary.
    #
    # db = dbm.open('databseFile', 'c')
    # # Record some values
    # db[b'hello'] = b'there'
    # db['www.python.org'] = 'Python Website'
    # db['www.cnn.com'] = 'Cable News Network'
    # print(db.get('www.python.org'))
    #
    # # Note that the keys are considered bytes now.
    # assert db[b'www.python.org'] == b'Python Website'
    # # Notice how the value is now in bytes.
    # assert db['www.cnn.com'] == b'Cable News Network'
    # print(1)
    # # Often-used methods of the dict interface work too.
    # print(db.get('python.org', 'not present'))
    # print(1)
    # k = db.firstkey()
    # while k != None:
    #     print(k)
    #     print(db.get(k).decode('ascii'))
    #
    #     k = db.nextkey(k)
    # # Storing a non-string key or value will raise an exception (most
    # # likely a TypeError).
    # db['www.yahoo.com'] = '4'
    # print(db['www.python.org'].decode('ascii'))
    # print(db['www.yahoo.com'].decode('ascii'))
    # print(db.get('www.yahoo.com', b'not present').decode('ascii'))
    #
    # # Close when done.
    # db.close()
