# -*- coding: utf-8 -*-
from watson.framework import applications
from wasapp.config import base as config

application = applications.Http(config)

print('init db')
print('file created')
