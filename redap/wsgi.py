# -*- coding: utf-8 -*-

import sys
import logging
import warnings
from redap.exceptions import InvalidConfiguration

try:
    from .api import create_app

    with warnings.catch_warnings():
        # Ignore Flask deprecation warnings
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    app = create_app()


except InvalidConfiguration as error:
    root = logging.getLogger()
    root.critical("Configuration file '{0}' failed validation: \n{1}".format(error.file, error.cause))
    sys.exit(4)
