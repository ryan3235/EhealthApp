# # -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
from wasapp.db import sqliteDB

class Putdata(controllers.Rest):
    def GET(self):
        print('in putdata controller')
        userName = self.request.get['userName']
        password = self.request.get['pass']
        deviceID = self.request.get['dID']
        temperature = self.request.get['temp']
        humidity = self.request.get['humi']
        
        sql='SELECT * FROM user where username = \''+self.request.get['userName']+'\' AND password=\''+self.request.get['pass']+'\'' 
        print(sql)
        result=sqliteDB().query(sql)
        result=result.fetchall()
        uid=0
        if(len(result)>0):
            uid=result[0][0]
        

        sql='SELECT * FROM device where dID = \''+self.request.get['dID']+'\'' 
        print(sql)
        result=sqliteDB().query(sql)
        result=result.fetchall()
        dID=0
        if(len(result)>0):
            dID=result[0][0]

        print('uid:'+str(uid)+' dID:'+str(dID))

        if(uid>0 and dID>0):
            sql='INSERT INTO eviDataTimeStamp VALUES (datetime(\'now\'), datetime(\'now\', \'localtime\'), '+self.request.get['dID']+','+self.request.get['temp']+','+self.request.get['humi']+');' 
            print(sql)
            print('\n')
            result=sqliteDB().insertQuery(sql)
            pass
        # sql='SELECT * FROM eviDataTimeStamp' 
        # print(sql)
        # result=sqliteDB().query(sql)   
        # for row in result:
        #     print ("evi")
        #     print (row)



        print(userName+password+deviceID+temperature+humidity)
        return userName+password+deviceID+temperature+humidity

#         # temperature and humidity
#
#     # //putdata/?userName=myUN&pass=mypass&dID=202&temp=25&humi=50%
# -*- coding: utf-8 -*-
# from watson import framework
# from watson.framework import controllers
#
#
# class Putdata(controllers.Rest):
#     def GET(self):
#         query = self.request.get['query']
#         val = self.request.get['value']
#         print('in data controller')
#         # print(query+val)
#         return 'Welcome to Watson v{0}! index'.format(framework.__version__)
