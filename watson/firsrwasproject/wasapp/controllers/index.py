# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
# from flask import Flask, render_template

# from wasapp.db import testfunction

class Index(controllers.Rest):
    def GET(self):
        query = self.request.get['query']
        val = self.request.get['value']
        print('in index controller')
        

        # print(query+val)
        # testfunction(1)
        # return 'Welcome to Watson v{0}! index'.format(framework.__version__)
        # return ('get.html',num=123)
        # return {'hello': (0,1,2),'hi': (4,5,6)}
        # return 'hello'=(1,2,3)
        return {'hello': [2,3,4]}