# -*- coding: utf-8 -*-
from watson.framework import applications
from wasapp.config import base as config
from wasapp.db import sqliteDB
application = applications.Http(config)

# checkTables();
