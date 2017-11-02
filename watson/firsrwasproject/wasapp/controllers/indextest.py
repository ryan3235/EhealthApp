# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
from watson.framework.views.decorators import view
# from flask import Flask, render_template

# from wasapp.db import testfunction

class Indextest(controllers.Rest):
    @view(format='json')
    def GET(self):
        query = self.request.get['query']
        val = self.request.get['value']
        print('in indextest controller')
        return {'key': 'Index test done'}