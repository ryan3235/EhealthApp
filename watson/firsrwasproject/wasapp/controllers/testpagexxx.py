# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Testpage(controllers.Rest):
    def GET(self):
        print('in test controller')
        print('new line test')
        # self.response = '23s'
        # print('Welcome to testPage v{0}!'.format(framework.__version__))
        # return json.dumps({'123':123})
        # return{'flash_messages': self.flash_messages}
        # controllers._response
        # render 
    
    def PUT(self):
        data = self.request.post['data']
        print(data)
        pass


# 'putdata':{'path': '/putdata', 'options': {'controller': 'wasapp.controllers.Putdata'}},
