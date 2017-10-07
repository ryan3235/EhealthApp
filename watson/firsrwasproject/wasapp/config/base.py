# -*- coding: utf-8 -*-
"""Define and extend configuration settings for your application.
"""

import os
from wasapp.config.routes import routes  # noqa
from wasapp.config.dependencies import dependencies  # noqa


debug = {
    'enabled': os.environ.get('DEV_ENV', False)
}
