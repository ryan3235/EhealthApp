# -*- coding: utf-8 -*-
"""Create routes for your application here.
"""
routes = {
    'index': {'path': '/','options': {'controller': 'wasapp.controllers.Index'}},
    'testpage':{'path':'/testpage','options': {'controller': 'wasapp.controllers.Testpage'}},
    'bpm':{'path':'/bpm','options': {'controller': 'wasapp.controllers.Bpm'}},
    'login':{'path':'/login','options': {'controller': 'wasapp.controllers.Login'}},
 # 'route_test': {'path': '/resource','accepts': ('GET', 'POST')'options': {'controller': 'wasapp.controllers.Resource'}}
    'MyHome':{'path':'/myData','options': {'controller': 'wasapp.controllers.Mydata'},'defaults': {'format': 'json'}}
}
#controllerBpm
