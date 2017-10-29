# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import dbm
import sqlite3
# Open database, creating it if necessary.


# def testfunction(dataarray):

#     conn = sqlite3.connect('example.db')
#     c = conn.cursor()

#     # Create table
#     c.execute('''CREATE TABLE stocks
#                  (date text, trans text, symbol text, qty real, price real)''')

#     # Insert a row of data
#     c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#     # Save (commit) the changes
#     conn.commit()
#     for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#         print (row)
#     # We can also close the connection if we are done with it.
#     # Just be sure any changes have been committed or they will be lost.
#     conn.close()

class sqliteDB:
    conn = None
    def connect(self):
        print('checking databse file')
        self.conn = sqlite3.connect('Ehealth.db')
        c = self.conn.cursor()
        print('checking tables')

        #建立新表 保存用户的年龄等信息
        c.execute('''CREATE TABLE IF NOT EXISTS user(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username text,
            password text,
            usernickname text,
            userAge text,
            rheumatoidAge text,
            email text,
            city text)''')

        c.execute('''CREATE TABLE IF NOT EXISTS device
                    (dID INTEGER PRIMARY KEY, uid INTEGER, dName text, dDiscription text)''')

        c.execute('''CREATE TABLE IF NOT EXISTS eviDataTimeStamp
                    (dtime text, dtimelocation text, dID INTEGER, temp real, humi real,PRIMARY KEY (dtime, dtimelocation, dID))''')
        self.conn.commit()
        # for row in c.execute('SELECT * FROM user'):
        #     print ("user infor")
        #     print (row)

        # for row in c.execute('SELECT * FROM device'):
        #     print ("device infor")
        #     print (row)


    def query(self, sql):
        try:
            c = self.conn.cursor()
            print('execute sql '+sql)
            c.execute(sql)
            
        except (AttributeError):
            print('Connecting database')
            self.connect()
            c = self.conn.cursor()
            c.execute(sql)
            # self.conn.close()
        return c
    def insertQuery(self, sql):
        try:
            c = self.conn.cursor()
            print('execute sql '+sql)
            c.execute(sql)
        
        except (AttributeError):
            print('Connecting database')
            self.connect()
            c = self.conn.cursor()
            c.execute(sql)
            self.conn.commit()
            # self.conn.close()
        return c
    




# db = sqliteDB()
# sql = 'SELECT * FROM user'
# cur = db.query(sql)
# cur = db.query(sql)




# # wait a long time for the Mysql connection to timeout
# cur = db.query(sql)
# for row in cur:
#     print ("user infor")
#     print (row)

    