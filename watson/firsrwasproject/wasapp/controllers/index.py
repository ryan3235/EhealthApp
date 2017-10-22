# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers

# from wasapp.db import testfunction

class Index(controllers.Rest):
    def GET(self):
        query = self.request.get['query']
        val = self.request.get['value']
        print('in index controller')
        

        # print(query+val)
        # testfunction(1)
        return 'Welcome to Watson v{0}! index'.format(framework.__version__)
