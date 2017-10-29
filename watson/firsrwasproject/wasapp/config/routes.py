# -*- coding: utf-8 -*-
"""Create routes for your application here.
"""
routes = {
    'index': {'path': '/','options': {'controller': 'wasapp.controllers.Index'}},
    'testpage':{'path':'/testpage','options': {'controller': 'wasapp.controllers.Testpage'}},
    'showData':{'path':'/showData','options': {'controller': 'wasapp.controllers.ShowData'}},
    'login':{'path':'/login','options': {'controller': 'wasapp.controllers.Login'}},
    'putdata':{'path':'/putdata','options': {'controller': 'wasapp.controllers.Putdata'}},
    'signup':{'path':'/signUp','options': {'controller': 'wasapp.controllers.Signup'}},
    'generatemap':{'path':'/generatemap', 'options':{'controller':'wasapp.controllers.Generatemap'}}
 # 'route_test': {'path': '/resource','accepts': ('GET', 'POST')'options': {'controller': 'wasapp.controllers.Resource'}}
 #    'MyHome':{'path':'/myData','options': {'controller': 'wasapp.controllers.Mydata'},'defaults': {'format': 'json'}}
}
#controllerBpm
# 'testpage':{'path':'/testpage','options': {'controller': 'wasapp.controllers.Testpage'}},
