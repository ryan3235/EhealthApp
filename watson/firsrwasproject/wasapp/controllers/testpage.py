# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Testpage(controllers.Rest):
    def GET(self):
        print('in test controller')
        # print('Welcome to testPage v{0}!'.format(framework.__version__))
        return 'Welcome to testPage v{0}!'.format(framework.__version__)
    def PUT(self):
        data = self.request.post['data']
        print(data)
        pass
