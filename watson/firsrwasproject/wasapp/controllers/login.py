# from watson.framework import controllers
# from app import forms
#
# class Login(controllers.Rest):
#     def GET(self):
#         form = forms.Login('login_form', action='/login')
#         form.data = self.redirect_vars
#         # populate the form with POST'd data to avoid the PRG issue
#         # we don't really need to do this
#         return {
#             'form': form
#         }
# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Login(controllers.Rest):
    def GET(self):
        print('in login controller')
        print('Welcome to Watson v{0}!'.format(framework.__version__))
        # return 'Welcome to Watson v{0}! index'.format(framework.__version__)
        return 'login page '
