# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Bpm(controllers.Rest):
    def GET(self):
        print('in bpm controller')
        print('xxxxx\n')
        return 'Welcome to Watson v{0}! bpm'.format(framework.__version__)
    def POST(self):
        data = self.request.post
        # print('in post and count is ')
        return 888
