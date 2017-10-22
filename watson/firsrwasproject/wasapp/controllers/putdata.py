# # -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Putdata(controllers.Rest):
    def GET(self):
        print('in putdata controller')
        userName = self.request.get['userName']
        password = self.request.get['pass']
        deviceID = self.request.get['dID']
        temperature = self.request.get['temp']
        humidity = self.request.get['humi']

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
