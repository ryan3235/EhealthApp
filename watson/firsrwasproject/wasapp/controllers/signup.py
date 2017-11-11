# # -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
from wasapp.db import sqliteDB

class Signup(controllers.Rest):
    def GET(self):
        if 'userName' in self.request.get:
            print('in putdata controller')
            userName = self.request.get['userName']
            password = self.request.get['pass']
            userNicname = self.request.get['userNicname']
            age = self.request.get['userAge']
            rheumatoidAge = self.request.get['rheumatoidAge']
            email = self.request.get['email']
            city = self.request.get['city']
            dName = self.request.get['dName']
            dID = self.request.get['dID']
            dd = self.request.get['dd']
            
            sql='SELECT * FROM user where username = \''+self.request.get['userName']+'\''
            print(sql)
            result=sqliteDB().query(sql)
            result=result.fetchall()
            if(len(result)==0):
                # regi
                sql='INSERT INTO user (username,password,usernickname,userAge,rheumatoidAge,email,city) VALUES (\''+userName+'\',\''+password+'\',\''+userNicname+'\',\''+age+'\',\''+rheumatoidAge+'\',\''+email+'\',\''+city+'\')';
                print(sql)
                print('\n')
                result=sqliteDB().insertQuery(sql)
            sql='SELECT * FROM user where username = \''+self.request.get['userName']+'\''
            print(sql)
            result=sqliteDB().query(sql)
            result=result.fetchall()
            uid=result[0][0]

            print(str(uid)+'____ is UID'+ '__dID='+dID)

            sql='INSERT INTO device (dID,uid,dName,dDiscription) VALUES ('+dID+','+str(uid)+',\''+dName+'\',\''+dd+'\')';
            print(sql)
            print('\n')
            result=sqliteDB().insertQuery(sql)
            
            
            if uid>0:
                self.redirect('/login')
            else:
                return 'Something when worng, please try again'

            
        else:
            # self.redirect('/','Please login before use.')  
            self.redirect('/')
