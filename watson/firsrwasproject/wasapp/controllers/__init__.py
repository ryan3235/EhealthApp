# # -*- coding: utf-8 -*-


# from watson.framework import controllers
from wasapp.controllers.index import Index
#
#
# __all__ = ['Index']
from wasapp.controllers.testpage import Testpage

from wasapp.controllers.showdata import ShowData
from wasapp.controllers.login import Login
from wasapp.controllers.putdata import Putdata
from wasapp.controllers.signup import Signup

from wasapp.controllers.generatemap import Generatemap


# test classes
from wasapp.controllers.indextest import Indextest
from wasapp.controllers.showdatatest import ShowDatatest
from wasapp.controllers.logintest import Logintest
from wasapp.controllers.putdatatest import Putdatatest
from wasapp.controllers.signuptest import Signuptest



# from wasapp import forms

# class testpage(controllers.Rest):#controller file name
#     def GET(self):
#         # print(id)
#         # # return {
#         # #
#         # # }
#         #this
#         #__all__
#         # print('after testpage')
#         # return 'testpage'
#         pass
#
#     def POST(self):
#         pass
#
#     def PUT(self):
#         pass
#
#     def DELETE(self):
#         pass
#
# class index(controllers.Rest):#controller file name
#     def GET(self):
#         # print('running init in Index')
#         # this = ['Index']
#         # print('after Index')
#         pass
#
#     def POST(self):
#         pass
#
#     def PUT(self):
#         pass
#
#     def DELETE(self):
#         pass
#
#
# class controllerBpm(controllers.Rest):#controller file name
#     def GET(self):
#         # print('running init in Bpm')
#         # this = ['Bpm']
#         # print('after bpm')
#         pass
#
#     def POST(self):
#         pass
#
#     def PUT(self):
#         pass
#
#     def DELETE(self):
#         pass
#
