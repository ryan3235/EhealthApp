# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
import json

class Testpage(controllers.Rest):
    def GET(self):
        print('in test controller')
	return json.dumps({'123':123})
    
    def PUT(self):
        data = self.request.post['data']
        print(data)
        pass


# 'putdata':{'path': '/putdata', 'options': {'controller': 'wasapp.controllers.Putdata'}},
