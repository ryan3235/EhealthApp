# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
from wasapp.db import sqliteDB
from datetime import datetime


class ShowData(controllers.Rest):
    
    # def dateformator(self,dateString):
    #     a = datetime.strptime(dateString, '%Y-%m-%d-%H-%M-%S')
    #     return (a.timestamp() * 1000)
    
    def GET(self):
        # print('in bpm controller')
        # print('xxxxx\n')
        if 'userName' in self.request.get:
            sql='SELECT * FROM user where username = \''+self.request.get['userName']+'\' AND password=\''+self.request.get['pass']+'\'' 
            print(sql)
            result=sqliteDB().query(sql)
            result=result.fetchall()
            uid=0
            if(len(result)>0):
                uid=result[0][0]

            sql='SELECT * FROM device where uid = \''+str(uid)+'\'' 
            print(sql)
            result=sqliteDB().query(sql)
            result=result.fetchall()
            dID=0
            
            for dinfor in result:
                dID=dinfor[0]
                print(dID)
                sql='SELECT dtimelocation as mytime, temp, humi  FROM eviDataTimeStamp where dID = \''+str(dID)+'\''
                newResult=sqliteDB().query(sql)
                
                listDiction={}
                # print(newResult)
                eviDataResult=[]
                for each in newResult:
                    a = datetime.strptime(each[0], '%Y-%m-%d %H:%M:%S')
                    eviDataResult.append((int(a.timestamp() * 1000),each[1],each[2]))
                listDeviceID=eviDataResult[0][0]
                listDiction[str(dID)]=eviDataResult


            # print(listDiction)
            # for each in listDiction:
            #     print(each)
            return {'Sensordata': listDiction}
        else:
            return 'Welcome to Watson v{0}! bpm'.format(framework.__version__)
          
    
    



        
    def POST(self):
        data = self.request.post
        # print('in post and count is ')
        return 888
