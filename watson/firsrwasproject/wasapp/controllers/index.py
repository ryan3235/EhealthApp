# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Index(controllers.Rest):
    def GET(self):
        print('in index controller')
        print('Welcome to Watson v{0}!'.format(framework.__version__))
        return 'Welcome to Watson v{0}! index'.format(framework.__version__)
