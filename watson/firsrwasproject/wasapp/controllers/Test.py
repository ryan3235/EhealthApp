from watson.di import ContainerAware
from watson.framework import listeners
from watson.framework import controllers
from watson import form
from watson.form import fields

class MyFirstListener(form.Form):
    def __call__(self, event):
        # we'll perform something based on the event and target here
        pass