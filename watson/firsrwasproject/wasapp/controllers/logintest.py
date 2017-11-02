from watson import framework
from watson.framework import controllers
from watson.framework.views.decorators import view


class Logintest(controllers.Rest):
    @view(format='json')
    def GET(self):
        print('in logintest controller')
        return {'key': 'Login test done'}

