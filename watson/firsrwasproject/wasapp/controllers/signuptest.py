# # -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
from wasapp.db import sqliteDB
from watson.framework.views.decorators import view

class Signuptest(controllers.Rest):
    @view(format='json')
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
                # if user have not been found add the user and device
                return {'key':'User not found, inseted into database and redirect to the Dashboard'}
            else:
                return {'key':'User has been found, not inserting'}
                

            
        else:
            # self.redirect('/','Please login before use.')  
             return {'key':'User name was not been sbminted pleas try it again'}
